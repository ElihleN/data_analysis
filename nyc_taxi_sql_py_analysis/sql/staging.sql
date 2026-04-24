CREATE SCHEMA IF NOT EXISTS staging;

-- Basic row count
SELECT COUNT(*) AS total_rows
FROM staging.yellow_taxi_raw;

-- Column completeness check
SELECT
    COUNT(*) AS total_rows,
    COUNT(vendorid) AS vendorid_non_null,
    COUNT(tpep_pickup_datetime) AS pickup_non_null,
    COUNT(tpep_dropoff_datetime) AS dropoff_non_null,
    COUNT(passenger_count) AS passenger_count_non_null,
    COUNT(trip_distance) AS trip_distance_non_null,
    COUNT(fare_amount) AS fare_amount_non_null,
    COUNT(total_amount) AS total_amount_non_null
FROM staging.yellow_taxi_raw;

-- Quick data quality scan
SELECT *
FROM staging.yellow_taxi_raw
WHERE trip_distance < 0
   OR fare_amount < 0
   OR total_amount < 0
LIMIT 20;

-- Pickup datetime range
SELECT
    MIN(tpep_pickup_datetime) AS min_pickup,
    MAX(tpep_pickup_datetime) AS max_pickup
FROM staging.yellow_taxi_raw;


SELECT * FROM staging.yellow_taxi_raw LIMIT 10;

SELECT
    COUNT(*) AS total_rows,
    COUNT(DISTINCT PULocationID) AS unique_pickup_zones,
    COUNT(DISTINCT DOLocationID) AS unique_dropoff_zones
FROM staging.yellow_taxi_raw;

SELECT
    payment_type,
    COUNT(*) AS trips
FROM staging.yellow_taxi_raw
GROUP BY payment_type
ORDER BY trips DESC;