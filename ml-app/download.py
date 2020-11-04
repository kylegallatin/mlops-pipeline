import os
import boto3

s3 = boto3.client('s3', aws_access_key_id=os.environ['AWS_KEY'], aws_secret_access_key=os.environ['AWS_SECRET_KEY'])
s3.download_file('dseiasvslmldevamrasp115260', 'mlflow/19/e09019d869ff40ceb2825ef41e1f79b3/artifacts/rf-regressor/model.pkl', 'model.pkl')