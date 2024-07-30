FROM python:3.10-slim

WORKDIR /opt/app

ENV ENV=prod
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY src src

EXPOSE 8080
WORKDIR /opt/app/src
CMD [ "python3", "-u", "main.py" ]