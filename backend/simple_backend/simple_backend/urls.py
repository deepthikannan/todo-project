"""simple_backend URL Configuration
"""
from django.conf.urls import url
from django.contrib import admin
from tasks.views import task_list

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tasks/', task_list),
]

