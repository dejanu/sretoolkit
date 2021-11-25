FROM python:3-alpine

# We copy just the requirements.txt first to leverage Docker cache
COPY requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 8880
ENV LB_URL=https://lb01.cura.columna.dk:9070/api/tm/8.0/status/local_tm/state/
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]