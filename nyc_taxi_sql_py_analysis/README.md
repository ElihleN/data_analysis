# NYC Taxi SQL Pipeline Project

## Overview

This project builds a SQL-first analytics pipeline using the official NYC Taxi & Limousine Commission (TLC) Yellow Taxi trip dataset.

Instead of manually downloading CSV files, the pipeline queries monthly Parquet files directly from the official source and stages them using DuckDB. The workflow simulates a production-style ingestion pipeline with staging, transformation, and analytics layers.

## Objectives

- demonstrate remote data ingestion from official public datasets
- build a reproducible SQL staging pipeline
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
- load_to_mysql.py

sql/

- staging.sql
- marts.sql
- analytics_queries.sql

data/

- optional local artifacts and lookup tables

## Data Source

NYC Taxi & Limousine Commission (TLC)

https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

Trip records are published monthly as Parquet files and accessed directly via HTTP using DuckDB.

## Pipeline Architecture

Raw Parquet (remote)
↓
staging.yellow_taxi_raw
↓
staging.yellow_taxi_clean
↓
analytics marts table

