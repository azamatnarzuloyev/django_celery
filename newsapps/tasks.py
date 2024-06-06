from celery import shared_task
from datetime import datetime
from time import sleep
import requests

@shared_task
def task1(sleeptime):
    sleep(5)
    print("hello")
    return None

@shared_task
def task2():
    print("hello")
    return 