import duckdb

DB_PATH = "nyc_taxi_pipeline.duckdb"


def main():
    con = duckdb.connect(DB_PATH)

    con.execute("CREATE SCHEMA IF NOT EXISTS staging;")
    con.execute("DROP TABLE IF EXISTS staging.yellow_taxi_clean;")

    con.execute("""
        CREATE TABLE staging.yellow_taxi_clean AS
        WITH base AS (
            SELECT
                VendorID,
                tpep_pickup_datetime,
                tpep_dropoff_datetime,
                passenger_count,
                trip_distance,
                RatecodeID,
                store_and_fwd_flag,
                PULocationID,
                DOLocationID,
                payment_type,
                fare_amount,
                extra,
                mta_tax,
                tip_amount,
                tolls_amount,
                improvement_surcharge,
                total_amount,
                congestion_surcharge,
                Airport_fee,
                datediff('minute', tpep_pickup_datetime, tpep_dropoff_datetime) AS trip_duration_minutes
            FROM staging.yellow_taxi_raw
            WHERE
                tpep_pickup_datetime IS NOT NULL
                AND tpep_dropoff_datetime IS NOT NULL
                AND tpep_dropoff_datetime >= tpep_pickup_datetime
                AND passenger_count > 0
                AND trip_distance > 0
                AND fare_amount >= 0
                AND total_amount >= 0
        )
        SELECT
            b.VendorID,
            b.tpep_pickup_datetime,
            b.tpep_dropoff_datetime,
            b.passenger_count,
            b.trip_distance,
            b.RatecodeID,
            b.store_and_fwd_flag,
            b.PULocationID,
            b.DOLocationID,
            pu.Borough AS pickup_borough,
            pu.Zone AS pickup_zone,
            pu.service_zone AS pickup_service_zone,
            do.Borough AS dropoff_borough,
            do.Zone AS dropoff_zone,
            do.service_zone AS dropoff_service_zone,
            b.payment_type,
            b.fare_amount,
            b.extra,
            b.mta_tax,
            b.tip_amount,
            b.tolls_amount,
            b.improvement_surcharge,
            b.total_amount,
            b.congestion_surcharge,
            b.Airport_fee,

            DATE(b.tpep_pickup_datetime) AS pickup_date,
            YEAR(b.tpep_pickup_datetime) AS pickup_year,
            MONTH(b.tpep_pickup_datetime) AS pickup_month,
            DAY(b.tpep_pickup_datetime) AS pickup_day,
            HOUR(b.tpep_pickup_datetime) AS pickup_hour,
            DAYNAME(b.tpep_pickup_datetime) AS pickup_weekday,

            DATE(b.tpep_dropoff_datetime) AS dropoff_date,
            HOUR(b.tpep_dropoff_datetime) AS dropoff_hour,

            b.trip_duration_minutes,

            CASE
                WHEN b.trip_distance > 0 THEN b.total_amount / b.trip_distance
                ELSE NULL
            END AS revenue_per_mile,

            CASE
                WHEN b.fare_amount > 0 THEN b.tip_amount / b.fare_amount
                ELSE NULL
            END AS tip_pct_of_fare

        FROM base b
        LEFT JOIN staging.taxi_zone_lookup pu
            ON b.PULocationID = pu.LocationID
        LEFT JOIN staging.taxi_zone_lookup do
            ON b.DOLocationID = do.LocationID
        WHERE
            b.trip_duration_minutes BETWEEN 1 AND 180
            AND b.trip_distance BETWEEN 0.1 AND 100
            AND b.total_amount BETWEEN 1 AND 1000;
    """)

    clean_row_count = con.execute("""
        SELECT COUNT(*)
        FROM staging.yellow_taxi_clean;
    """).fetchone()[0]

    print(f"\nCreated staging.yellow_taxi_clean with {clean_row_count:,} rows")

    preview = con.execute("""
        SELECT
            pickup_borough,
            pickup_zone,
            dropoff_borough,
            dropoff_zone,
            trip_distance,
            total_amount,
            trip_duration_minutes
        FROM staging.yellow_taxi_clean
        LIMIT 10;
    """).fetchdf()

    print("\nPreview of enriched clean table:")
    print(preview)

    summary = con.execute("""
        SELECT
            COUNT(*) AS total_rows,
            COUNT(DISTINCT pickup_zone) AS unique_pickup_zones,
            COUNT(DISTINCT dropoff_zone) AS unique_dropoff_zones,
            AVG(trip_distance) AS avg_distance,
            AVG(total_amount) AS avg_total_amount,
            AVG(trip_duration_minutes) AS avg_duration
        FROM staging.yellow_taxi_clean;
    """).fetchdf()

    print("\nEnriched clean table summary:")
    print(summary)

    con.close()


if __name__ == "__main__":
    main()