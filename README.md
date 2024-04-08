# famProject
Youtube Video Listing

API for the Basic Work
v1/youtube/video/list/

To add Filter - we need to add params in this API like decription and title

Please clone the repo
docker compose build
docker compose up -- this will start a celery beat to hit the api in the backgeound and add the data in the database

if there is any issue in celery beat you can add the data using shell with the following command
from Youtube.utils import fetch_and_store_youtube_videos
fetch_and_store_youtube_videos() - this will add the data in the database, you can also program to run this in the interval of 10 sec


python manage.py runserver -- to start the seever
Please go the - http://127.0.0.1:8000/
There is a page with required response, here you get an option to see the video list
then the filter options and next page and previous page button


 I have already added a migration file
Please create a DB - famProjectDB 
and then run the migration file
python manage.py migrate

HOME PAGE
![HOME PAGE](https://github.com/aaryantyagi182/famProject/blob/main/famProject/home.jpg)
YOUTUBE LISITNG PAGE
![YOUTUBE LISITNG PAGE](https://github.com/aaryantyagi182/famProject/blob/main/famProject/youtubelist.png)
