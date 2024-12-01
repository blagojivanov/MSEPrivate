import time

from django.http import HttpResponse
from django.shortcuts import render
from api.utils.fetcher import pipeline


def index(request):
    return HttpResponse("Hello, world. You're at the API index.")


def update(request):
    start_time = time.time()
    pipeline()
    end_time = time.time()
    return HttpResponse(f"Data processing completed in {end_time - start_time} seconds")
