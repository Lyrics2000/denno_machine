
from django.contrib import admin
from django.urls import path
from .views import (
    index,
    map_filter,
    precipitation_prediction
)
app_name = "mainapp"
urlpatterns = [
    path('', index,name="index"),
    path("map_filter/",map_filter,name="map_filter"),
    path("precipitation_prediction/",precipitation_prediction,name="precipitation_prediction")


]

