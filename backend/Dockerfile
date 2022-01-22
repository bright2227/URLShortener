FROM python:3.8.12
LABEL maintainer bright.hsu
ENV PYTHONUNBUFFERED 1
RUN mkdir /backend

RUN apt-get -y update\
    && apt-get -y install vim

WORKDIR /backend
COPY . /backend
RUN python -m pip install --upgrade pip\
    && python3 -m pip install -r requirements.txt

RUN chmod a+x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
