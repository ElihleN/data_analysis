import duckdb

DB_PATH = "nyc_taxi_pipeline.duckdb"
SOURCE_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet"
DATASET_NAME = "yellow_taxi"
FILE_PERIOD = "2024-01"


def main():
    con = duckdb.connect(DB_PATH)

    # Enable remote file access
    con.execute("INSTALL httpfs;")
    con.execute("LOAD httpfs;")

    # Create schemas
    con.execute("CREATE SCHEMA IF NOT EXISTS metadata;")
    con.execute("CREATE SCHEMA IF NOT EXISTS staging;")

    # Create ingestion log table
    con.execute("""
        CREATE TABLE IF NOT EXISTS metadata.ingestion_log (
            dataset_name VARCHAR,
            file_period VARCHAR,
            source_url VARCHAR,
            loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            row_count BIGINT
        );
    """)

    # Optional: inspect schema before loading
    schema_preview = con.execute(f"""
        DESCRIBE
        SELECT *
        FROM read_parquet('{SOURCE_URL}')
    """).fetchdf()

    print("\nSchema preview:")
    print(schema_preview)

    # Drop and recreate raw staging table
    con.execute("DROP TABLE IF EXISTS staging.yellow_taxi_raw;")

    con.execute(f"""
        CREATE TABLE staging.yellow_taxi_raw AS
        SELECT *
        FROM read_parquet('{SOURCE_URL}');
    """)

    # Count loaded rows
    row_count = con.execute("""
        SELECT COUNT(*)
        FROM staging.yellow_taxi_raw;
    """).fetchone()[0]

    print(f"\nLoaded staging.yellow_taxi_raw with {row_count:,} rows")

    # Log this ingestion
    con.execute(f"""
        INSERT INTO metadata.ingestion_log (
            dataset_name,
            file_period,
            source_url,
            row_count
        )
        VALUES (
            '{DATASET_NAME}',
            '{FILE_PERIOD}',
            '{SOURCE_URL}',
            {row_count}
        );
    """)

    # Show ingestion log
    ingestion_log = con.execute("""
        SELECT *
        FROM metadata.ingestion_log
        ORDER BY loaded_at DESC;
    """).fetchdf()

    print("\nIngestion log:")
    print(ingestion_log)

    con.close()


if __name__ == "__main__":
    main()