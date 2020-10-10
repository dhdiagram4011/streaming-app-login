FROM digglerz/python3.8

MAINTAINER dhdiagram@gmail.com
EXPOSE 9002
WORKDIR /app
ADD . /app
RUN pip3 install djangorestframework
RUN pip3 install pymysql
RUN pip3 install Django==2.1.5
RUN pip3 install requests
RUN apt-get install wget -y
RUN wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.9.2-linux-x86_64.tar.gz
RUN tar xvf elasticsearch-7.9.2-linux-x86_64.tar.gz
RUN python3 manage.py migrate
RUN python3 manage.py makemigrations
CMD ["python3" ,"manage.py", "runserver", "0.0.0.0:9002"]