from celery import shared_task
import requests
from .models import News

@shared_task
def sync_data():

    url = "https://hacker-news.firebaseio.com/v0/topstories.json"

    response = requests.get(url)

    if response.status_code == 200:
            data = response.json()[:100]
            for item in data:
                News.objects.create(**item)
            print("Sync successful!")
            print(item[2])