# snowflake_loader/s3_to_snowflake.py
import snowflake.connector
import os

conn = snowflake.connector.connect(
    user='your_user',
    password='your_password',
    account='your_account_identifier',
    warehouse='your_warehouse',
    database='your_db',
    schema='your_schema',
    role='your_role'
)

cs = conn.cursor()

try:
    # Create file format (run once)
    cs.execute("""
        CREATE OR REPLACE FILE FORMAT json_format
        TYPE = 'JSON';
    """)

    # Create stage (run once)
    cs.execute("""
        CREATE OR REPLACE STAGE health_stage
        URL='s3://your-s3-bucket-name/health_data/'
        STORAGE_INTEGRATION = your_aws_integration
        FILE_FORMAT = json_format;
    """)

    # Create target table (if not already)
    cs.execute("""
        CREATE OR REPLACE TABLE health_data (
            user_id STRING,
            heart_rate NUMBER,
            temperature NUMBER,
            steps NUMBER,
            timestamp STRING
        );
    """)

    # Load data
    cs.execute("COPY INTO health_data FROM @health_stage FILE_FORMAT = (format_name = 'json_format');")

    print("Data copied from S3 to Snowflake successfully!")

finally:
    cs.close()
    conn.close()