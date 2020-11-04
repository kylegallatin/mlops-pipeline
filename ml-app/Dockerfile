FROM python:3.6

WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt

COPY ./model.pkl /app

COPY ./app.py .
CMD ["python","app.py"]