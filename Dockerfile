FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

ENV MONGODB_URL = "mongodb://localhost:27017"

EXPOSE 8000

CMD ["python3", "./app/main.py"]