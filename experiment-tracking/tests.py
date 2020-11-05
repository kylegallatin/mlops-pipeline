# https://raw.githubusercontent.com/darshikaf/mlflow-tracking-server-with-minio/master/tests/mlflow_client_test.py
import json
import os
from minio import Minio
from minio.error import ResponseError
import mlflow 
from random import random, randint

# TODO: clean directory structures in minIO

def set_env_vars():
    os.environ["MLFLOW_URL"] = "http://127.0.0.1:5000"
    os.environ["MLFLOW_S3_ENDPOINT_URL"] = "http://127.0.0.1:9000"
    os.environ["AWS_ACCESS_KEY_ID"] = "minio"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "minio123"


def create_s3_bucket():
    minioClient = Minio('127.0.0.1:9000',
                  access_key="minio",
                  secret_key="minio123",
                  secure=False)

    print(minioClient.list_buckets())

    try:
        if not minioClient.bucket_exists("testlocation"):
            minioClient.make_bucket('testlocation')
    except ResponseError as err:
        print(err)

    buckets = minioClient.list_buckets()
    for bucket in buckets:
        print(bucket.name, bucket.creation_date)

    policy = {"Version":"2012-10-17",
        "Statement":[
            {
            "Sid":"",
            "Effect":"Allow",
            "Principal":{"AWS":"*"},
            "Action":"s3:GetBucketLocation",
            "Resource":"arn:aws:s3:::testlocation"
            },
            {
            "Sid":"",
            "Effect":"Allow",
            "Principal":{"AWS":"*"},
            "Action":"s3:ListBucket",
            "Resource":"arn:aws:s3:::testlocation"
            },
            {
            "Sid":"",
            "Effect":"Allow",
            "Principal":{"AWS":"*"},
            "Action":"s3:GetObject",
            "Resource":"arn:aws:s3:::testlocation/*"
            },
            {
            "Sid":"",
            "Effect":"Allow",
            "Principal":{"AWS":"*"},
            "Action":"s3:PutObject",
            "Resource":"arn:aws:s3:::testlocation/*"
            }

        ]}

    minioClient.set_bucket_policy('testlocation', json.dumps(policy))

    # List all object paths in bucket that begin with my-prefixname.
    objects = minioClient.list_objects('testlocation', prefix='my',
                              recursive=True)
    for obj in objects:
        print(obj.bucket_name, obj.object_name.encode('utf-8'), obj.last_modified,
            obj.etag, obj.size, obj.content_type)

def train_model():
    #Connect to tracking server
    mlflow.set_tracking_uri("http://127.0.0.1:5000")

    # #Set experiment
    mlflow.set_experiment("/test-experiment")

    print(f"tracking_uri: {mlflow.get_tracking_uri()}")
    print(f"artifact_uri: {mlflow.get_artifact_uri()}")
    artifact_uri = mlflow.get_artifact_uri()

    # Create directory for artifacts
    if not os.path.exists("tests/data/artifact_folder"):
        os.makedirs("tests/data/artifact_folder")

    #Test parametes
    # with mlflow.start_run() as run:
    mlflow.log_param("param1", randint(0, 100))

    #Test metrics
    mlflow.log_metric("metric1", random())
    mlflow.log_metric("metric2", random())
    mlflow.log_metric("metric3", random())
    mlflow.log_metric("metric4", random())

    #Test tags
    mlflow.set_tag("tag", "version1")

    # Test artifact
    with open("tests/data/artifact_folder/test.txt", "w") as f:
        f.write("hello world!")
    mlflow.log_artifact("tests/data/artifact_folder/test.txt", "testlocation")

if __name__ == "__main__":
    # set_env_vars()
    print("Running the test script ...")
    # create_s3_bucket()
    train_model()