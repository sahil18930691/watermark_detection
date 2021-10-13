FROM python:3.8

ENV PYTHONUNBUFFERED 0

WORKDIR /watermark detection

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

ENV PORT="${PORT:-8080}"

CMD gunicorn main:app --bind 0.0.0.0:$PORT