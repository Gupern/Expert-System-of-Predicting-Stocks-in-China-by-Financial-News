FROM ubuntu:16.04

LABEL maintainer "guperner@hotmail.com"

ENV PROJECT_DIR=/opt/project/esps

WORKDIR $PROJECT_DIR

COPY ./requirements.txt $PROJECT_DIR 

RUN useradd labs && chown -R labs:labs $PROJECT_DIR 
RUN apt-get update -y \
 && apt-get upgrade -y \
 && apt-get install -y apt-utils \
 && apt-get install -y python3 \
 && apt-get install -y ttf-wqy-microhei \
 && apt-get install -y fontconfig xfonts-utils \
 && apt-get install -y unoconv \
 && apt-get install -y poppler-utils \
 && apt-get install -y vim git locales software-properties-common \
 && apt-get install -y build-essential libssl-dev libffi-dev python3-dev \
 && apt-get install -y python3-pip \
 && pip3 install --upgrade pip -i https://pypi.douban.com/simple/ \
 && pip3 install -r $PROJECT_DIR/requirements.txt -i https://pypi.douban.com/simple/ \
 && pip3 install tushare==0.8.2 -i https://pypi.douban.com/simple/ \
 && locale-gen zh_CN.UTF-8 \
 && update-locale LANG=zh_CN.UTF-8 \
 && rm -irf /var/lib/apt/lists/* \
 && rm -irf /var/cache/oracle-jdk8-installer

ENV LANG zh_CN.UTF-8
ENV LC_ALL zh_CN.UTF-8


