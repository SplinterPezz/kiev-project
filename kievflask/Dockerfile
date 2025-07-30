FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static

COPY ./requirements.txt /var/www/requirements.txt
COPY ./app /app/app
COPY ./main.py /app/main.py
COPY ./uwsgi.ini /app/uwsgi.ini

RUN apk --no-cache --update add bash nano \
  && pip install --upgrade pip \
  && apk --update add gcc \
  && apk --update add musl-dev \
  && apk --update add g++ \
  && pip install -r /var/www/requirements.txt