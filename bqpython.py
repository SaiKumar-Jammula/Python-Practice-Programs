from google.cloud import bigquery
from google.oauth2 import service_account

# Define your parameters

credentials_path = "C:/Users/JOKER/Downloads/sai-kumar-467607-c5f8feb9fbcf.json"
project_id = "sai-kumar-467607"
query = """
    SELECT * FROM `sai-kumar-467607.dea_db.loan_payments` LIMIT 10
"""

# Load credentials and initialize BigQuery client
credentials = service_account.Credentials.from_service_account_file(credentials_path)
client = bigquery.Client(credentials=credentials, project=project_id)

# Run the query
query_job = client.query(query)
results = query_job.result()

# Display results
for row in results:
    print(dict(row))  # converts Row object to dictionary for easy printing
