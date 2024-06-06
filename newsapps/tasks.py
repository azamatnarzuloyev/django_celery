from celery import shared_task
from datetime import datetime
from time import sleep
import requests
import time

@shared_task
def tp1(queue='celery'):
    time.sleep(5)
    print("task1")
    return None

@shared_task
def tp2(queue='celery:1'):
    time.sleep(15)
    print("task2")
    return 

@shared_task
def tp3(queue='celery:2'):
    time.sleep(20)
    print("task3")
    return 

@shared_task
def tp4(queue='celery:3'):
    print("hello")
    time.sleep(7)
    return