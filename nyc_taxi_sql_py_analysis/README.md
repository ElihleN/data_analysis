# NYC Taxi SQL Pipeline Project

## Overview

This project builds a SQL-first analytics pipeline using the official NYC Taxi & Limousine Commission (TLC) Yellow Taxi trip dataset.

Instead of manually downloading CSV files, the pipeline queries monthly Parquet files directly from the official source and stages them using DuckDB. 

## Objectives

- Ingest data remotely from official public datasets
- build a SQL staging pipeline
- clean and standardize transportation trip records
- model analytics-ready reporting tables
- simulate incremental monthly ingestion logic

## Tech Stack

DuckDB — remote parquet ingestion  
SQL — transformation and analytics queries  
Python — orchestration scripts  
MySQL — downstream warehouse layer (planned)

## Project Structure

scripts/

- ingest_yellow_taxi.py
- transform_taxi_data.py
- load_to_mysql.py (Upcoming)

sql/  (Upcoming)

- staging.sql
- marts.sql
- analytics_queries.sql

data/


## Data Source

NYC Taxi & Limousine Commission (TLC)

https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

Trip records are published monthly as Parquet files and accessed directly via HTTP using DuckDB.


