
from django.contrib import admin
from django.urls import path
from .views import (
    index,
    map_filter
)
app_name = "mainapp"
urlpatterns = [
    path('', index,name="index"),
    path("map_filter/",map_filter,name="map_filter")


]

