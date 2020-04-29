FROM python:3.7.7-alpine

COPY . /fampay
COPY requirements.txt /tmp

WORKDIR /tmp
RUN pip install --upgrade pip && pip install -r requirements.txt

WORKDIR ../fampay
RUN pwd && ls

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]