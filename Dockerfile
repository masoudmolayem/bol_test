FROM python:3.8
LABEL maintainer="Masoud Molayem <masoudmolayem@gmail.com>"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./bol /bol


WORKDIR /bol
EXPOSE 8000

RUN pip install -r /requirements.txt

