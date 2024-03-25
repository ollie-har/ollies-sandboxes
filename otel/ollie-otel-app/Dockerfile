# syntax=docker/dockerfile:1
FROM python:3.10-alpine

WORKDIR /app

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install --upgrade pip

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD app.py app.py

EXPOSE 4567
COPY . .
CMD ["flask", "run", "--debug"]