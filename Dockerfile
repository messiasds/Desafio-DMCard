FROM python:3.8-slim

WORKDIR /home/app_desafio

COPY . .

RUN pip install -r requiriments.txt

CMD python backend/run.py