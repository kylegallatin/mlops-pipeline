FROM python:3.7-slim-buster

RUN pip install mlflow boto3 pymysql minio sklearn cryptography

WORKDIR /training
COPY ./tests.py .
COPY ./kc_house_data.csv .
COPY ./train.py .
