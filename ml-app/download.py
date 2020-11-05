import os
import boto3

s3 = boto3.client('s3', aws_access_key_id=os.environ['AWS_KEY'], aws_secret_access_key=os.environ['AWS_SECRET_KEY'])
s3.download_file('bucket_name', 'mlflow/path/model.pkl', 'model.pkl')