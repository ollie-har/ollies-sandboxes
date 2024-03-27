# syntax=docker/dockerfile:1
FROM python:3.10-alpine

WORKDIR /app

RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install --upgrade pip

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD app.py app.py

EXPOSE 4567
COPY . .
CMD ["python3", "app.py"]