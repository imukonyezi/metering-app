# set the base image. Since we're running 
# a Python application a Python base image is used
FROM python:3.8
#FROM ubuntu:19.10
#RUN apt-get update -y && apt-get install -y python3-pip python3-dev
# set a key-value label for the Docker image
LABEL maintainer="Isaac Mukonyezi"
# copy files from the host to the container filesystem. 
# For example, all the files in the current directory
# to the  `/app` directory in the container

COPY . /app
#  defines the working directory within the container
WORKDIR /app
# set environment variables

#Prevents Python from copying pyc files to the container.
ENV PYTHONDONTWRITEBYTECODE 1

# Ensures that Python output is logged to the terminal, 
# making it possible to monitor Django logs in realtime.
ENV PYTHONUNBUFFERED 1

# run commands within the container. 
# For example, invoke a pip command 
# to install dependencies defined in the requirements.txt file. 
RUN pip install --upgrade pip
#RUN pip install -U virtualenv
RUN pip install virtualenv virtualenvwrapper

RUN virtualenv appenv
RUN ["/bin/bash", "-c", "source appenv/bin/activate"]
#RUN "source /usr/local/bin/virtualenvwrapper.sh && appenv/bin/activate"
RUN pip install --upgrade pip

RUN apt-get update
#RUN apt-get install mysql-server libmysqlclient-dev -y
#Docker requires us to use mariadb libs instead of mysql
RUN apt-get install mariadb-server libmariadb-dev-compat libmariadb-dev -y
RUN apt-get install apache2 libapache2-mod-wsgi-py3 -y
#RUN apt install python3-dev python3-pip
#RUN "source file" 


WORKDIR /app/djangosite
RUN pip install -r requirements.txt

# provide a command to run on container start. 
# For example, start the `app.py` application.
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]