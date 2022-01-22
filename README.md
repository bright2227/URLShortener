# URLShortener

DOMAIN_NAME為https://longurl2short.tk/，目前只開通以下兩個API

## How to init project

1. change and fill .env.example and sensitive.py.example to .env and sensitive.py

2. run  ```docker-compose up```

## Main Setting

1. URL_STORE_DURATION 網址保留秒數

2. CACHE_DURATION 網址保留在CACHE秒數

## API

1. 用短網址換長網址

   for example:

```
# request

GET: https://longurl2short.tk/api/shorturl/v1/MQ==

Content-Type: application/json

```
```
# response
{
    "long_url": "https://www.django-rest-framework.org/api-guide/serializers/"
}
```
2. 用長網址換短網址

   for example:

```
# request

POST: https://longurl2short.tk/api/shorturl/v1

Content-Type: application/json

BODY:
{
    "long_url": "https://www.django-rest-framework.org/api-guide/serializers/"
}
```
```
# response
{
    "short_url": "MQ=="
}
```

## TODO

1. Add vuejs frontend