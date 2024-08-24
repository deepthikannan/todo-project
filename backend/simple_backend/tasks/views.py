# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    task_names = [task.name for task in tasks]
    return JsonResponse(task_names, safe=False)

