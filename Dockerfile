FROM ubuntu:16.04

LABEL maintainer "guperner@hotmail.com"

ENV PROJECT_DIR=/opt/project/esps

WORKDIR $PROJECT_DIR

COPY ./requirements.txt $PROJECT_DIR 

RUN useradd labs && chown -R labs:labs $PROJECT_DIR 
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y apt-utils
RUN apt-get install -y python3
RUN apt-get install -y ttf-wqy-microhei
RUN apt-get install -y fontconfig xfonts-utils
RUN apt-get install -y unoconv
RUN apt-get install -y poppler-utils
RUN apt-get install -y vim git locales software-properties-common
RUN apt-get install -y build-essential libssl-dev libffi-dev python3-dev
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip -i https://pypi.douban.com/simple/
RUN pip3 install -r $PROJECT_DIR/requirements.txt -i https://pypi.douban.com/simple/
RUN locale-gen zh_CN.UTF-8
RUN update-locale LANG=zh_CN.UTF-8
RUN rm -irf /var/lib/apt/lists/*
RUN rm -irf /var/cache/oracle-jdk8-installer

ENV LANG zh_CN.UTF-8
ENV LC_ALL zh_CN.UTF-8


