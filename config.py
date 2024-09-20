# config.py
from google.auth import default
from google.cloud import bigquery

# Google Cloud authentication
credentials, project = default()

#credentials, _ = default(scopes=['https://www.googleapis.com/auth/cloud-platform'])

# Project settings
PROJECT_ID = "gemini-bq-test"
LOCATION = "us-central1"
REQUESTS_PER_MINUTE = 100

# BigQuery settings
dataset_id = 'gemini_demo'
table_name = 'delivery_metric_rows'
table_uri = f"bigquery://{PROJECT_ID}/{dataset_id}"

# Initialize BigQuery client
client = bigquery.Client(project=PROJECT_ID)
