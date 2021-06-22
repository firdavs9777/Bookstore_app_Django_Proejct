# Pull base image 
FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code 

# INSTALL DEPENDENCIES

COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system 

#COPY PROJECT 
COPY . /code/
