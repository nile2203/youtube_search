FROM python:3.7.7-alpine
ENV PYTHONUNBUFFERED 1

COPY . /fampay
COPY requirements.txt /tmp

RUN apk update && apk add postgresql-dev gcc python-dev musl-dev && pip install psycopg2-binary

WORKDIR /tmp
RUN pip install --upgrade pip && pip install --upgrade google-api-python-client oauth2client
RUN pip install -r requirements.txt

WORKDIR ../fampay

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]