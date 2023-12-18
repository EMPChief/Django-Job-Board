from django.contrib import admin
from django.urls import include, path
from .views import index, job_details

urlpatterns = [
    path('', index, name="home"),
    path('jobs/<int:id>/', job_details, name="job-details"),
]