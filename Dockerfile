FROM python:3.7-slim-buster

RUN pip install mlflow boto3 pymysql minio sklearn

COPY ./tests.py /
COPY ./ml-app/kc_house_data.csv /
COPY ./ml-app/train.py /