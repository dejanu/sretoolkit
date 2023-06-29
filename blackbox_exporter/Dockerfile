FROM python:3.8-slim-buster

WORKDIR /app

#COPY requirements. /app/requirements.txt
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_APP main.py
ENV FLASK_RUN_HOST=localhost
ENV FLASK_RUN_PORT=8088
EXPOSE 8088

CMD [ "python3", "main.py"]