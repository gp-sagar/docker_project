FROM python:3.10.4

WORKDIR /app

# RUN apk add 
# RUN apk update && apk add --no-cache mariadb-connector-c-dev build-base && pip3 install mysqlclient 
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /app