from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from news.models import Item


@require_http_methods(["GET"])
def index(request):
    items = Item.objects.all()
    return HttpResponse("Found the following items : {}\n".format([i.__str__() for i in items]))


@require_http_methods(["GET"])
def get_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return HttpResponse("Found item {}".format(item))


@require_http_methods(["POST"])
def create_item(request):
    item = Item()
    if request.POST.get("text"):
        item.text = request.GET.get("text")
    else:
        item.title = request.POST.get("title")
        item.url = request.POST.get("url")
    item.save()
    return HttpResponse("Created item {}".format(item))


@require_http_methods(["POST"])
def delete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item.delete()
    return HttpResponse("Deleted item id {}".format(item_id))
