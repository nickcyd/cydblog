# coding: utf-8

import datetime
from django.shortcuts import render


def index(request):
    now = datetime.datetime.now()
    c_time = now.strftime("%Y-%m-%d %X")
    return render(request, 'index.html', {'c_time': c_time})
