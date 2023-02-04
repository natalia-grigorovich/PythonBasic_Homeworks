# Команда для запуска:
# docker run -it -p 8000:8000 app

FROM python:3.9-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY homework_03 .

EXPOSE 8000

CMD uvicorn main:app --host 0.0.0.0
