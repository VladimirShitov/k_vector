from django.shortcuts import render

from pathology.views import index as pathology_index


def index(request):
    return pathology_index(request)
