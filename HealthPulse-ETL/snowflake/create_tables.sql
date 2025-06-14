USE DATABASE DEMO;
USE SCHEMA PUBLIC;
USE WAREHOUSE COMPUTE_WH;

CREATE OR REPLACE TABLE health_data_raw (
    user_id STRING,
    heart_rate NUMBER,
    steps NUMBER,
    sleep_hours FLOAT,
    calories_burned NUMBER,
    timestamp TIMESTAMP
);

CREATE OR REPLACE FILE FORMAT json_format
TYPE = 'JSON';

CREATE OR REPLACE STORAGE INTEGRATION s3_healthpulse_integration
TYPE = EXTERNAL_STAGE
STORAGE_PROVIDER = 'S3'
ENABLED = TRUE
STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::767397922128:role/healthpulse-s3-access-role'
STORAGE_ALLOWED_LOCATIONS = ('s3://healthpulse-etl-bucket/health_data/');

DESC INTEGRATION s3_healthpulse_integration;

CREATE OR REPLACE STAGE s3_healthpulse_stage
URL = 's3://healthpulse-etl-bucket/health_data/'
STORAGE_INTEGRATION = s3_healthpulse_integration
FILE_FORMAT = json_format;

COPY INTO health_data_raw
FROM @s3_healthpulse_stage
FILE_FORMAT = (FORMAT_NAME = json_format)
MATCH_BY_COLUMN_NAME = CASE_INSENSITIVE
PATTERN = '.*\\.json'

LIST @s3_healthpulse_stage;

SELECT *
FROM health_data_raw 

TRUNCATE health_data_raw;