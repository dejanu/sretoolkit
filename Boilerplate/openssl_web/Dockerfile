FROM python:3-alpine
WORKDIR /code
ENV FLASK_APP=app
#ENV FLASK_RUN_HOST=0.0.0.0
COPY . /code
RUN pip install -r requirements.txt
EXPOSE 8080
COPY . .
CMD ["flask", "run","--host=0.0.0.0","--port=8080"]