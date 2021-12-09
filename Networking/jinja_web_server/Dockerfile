FROM python:3-alpine

# We copy just the requirements.txt first to leverage Docker cache
COPY requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 9095
ENV LB_URL=https://loadbalance.stuff
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
