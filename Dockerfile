FROM python:slim-buster

# ENV APP 'crawler.py'

COPY . /app/

RUN apt-get update \
    && apt-get install -y binutils libproj-dev gdal-bin \
    && apt-get install -y software-properties-common \
    && add-apt-repository ppa:ubuntugis/ppa \
    && apt-get install -y libgeos++-dev \
    && apt-get install -y proj-bin \
    && apt-get install -y gdal-bin \
    && apt-get install -y libgdal-dev

WORKDIR /app/myservicearea

RUN pip install -r ../requirements.txt

# RUN python manage.py migrate
CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8000"]