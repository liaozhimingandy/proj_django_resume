FROM python:3.9-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories \
    && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev \
    tiff-dev tk-dev tcl-dev harfbuzz-dev fribidi-dev jpeg g++

RUN pip install -U pip setuptools wheel -i https://mirrors.aliyun.com/pypi/simple/ || \
    pip install -U pip setuptools wheel

RUN mkdir /opt/app
WORKDIR /opt/app
COPY . /opt/app    

RUN pip install -i https://mirrors.aliyun.com/pypi/simple/ -r /opt/app/requirements.txt || \
    pip install -r /opt/app/requirements.txt
    
RUN rm -rf /opt/app/db.sqlite3 \
    && mv /opt/app/proj_django_resume/settings_for_docker.py  /opt/app/proj_django_resume/settings.py \
    && rm -rf .git \
    && rm -rf .gitignore \
    && rm -rf img

RUN ["rm", "-fr", "/opt/app/db.sqlite3"]
RUN ["chmod", "+x", "/opt/app/config/entrypoint.sh"]

# run entrypoint.sh
ENTRYPOINT ["/opt/app/config/entrypoint.sh"]
