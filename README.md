This is a basic project to get the video data from youtube using the search:list api. The data is fetched using a async task which gets the data every 30 seconds and store into the database. 

There are 2 APIs. The details are listed below:

1. Initiate youtube search data get task: This API would initiate the background task for getting the data
2. Search API - This API would get the data from the database retrieved from the above task

The entire project is dockerize. The steps needed to get started are below:

1. Clone the respository
2. docker-compose build in the main directory where Dockerfile is present
3. Make the database using with name, username, password - fampay
  1. psql 
  2. create database fampay;
  3. create user fampay with password 'fampay';
  4. grant all privileges on fampay to fampay;
4. docker-compose run python python manage.py migrate - for installing the migrations
3. docker-compose up in the main directory where docker-compose.yml

You are good to go!

