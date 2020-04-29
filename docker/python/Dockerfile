FROM python:3.7.7-alpine
ENV PYTHONUNBUFFERED 1

COPY . /fampay
COPY requirements.txt /tmp

RUN apk update && apk add postgresql-dev gcc python-dev musl-dev && pip install psycopg2-binary

WORKDIR /tmp
RUN pip install --upgrade pip && pip install -r requirements.txt

WORKDIR ../fampay
RUN pwd && ls

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]