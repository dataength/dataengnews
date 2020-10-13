from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from news.models import Item


@require_http_methods(["GET"])
def index(request):
    items = Item.objects.all()
    return HttpResponse("Found the following items : {}\n".format([i.__str__() for i in items]))
