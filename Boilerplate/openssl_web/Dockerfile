FROM python:3.8-alpine
WORKDIR /code
ENV FLASK_APP=app
#ENV FLASK_RUN_HOST=0.0.0.0
COPY . /code
# fix error: command 'gcc' failed with exit status 1 error: command 'gcc' failed with exit status 1
RUN apk --update --upgrade add gcc musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev
RUN apk add libressl-dev openssl
# ERROR: Failed building wheel for cffi
RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
    && pip install --no-cache-dir -r /code/requirements.txt \
    && apk del .build-deps
RUN pip install -r requirements.txt
EXPOSE 8080
COPY . .
CMD ["flask", "run","--host=0.0.0.0","--port=8080"]