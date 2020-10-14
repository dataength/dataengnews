from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>/', views.get_item, name='get_item'),
    path('create/', views.create_item, name='create_item'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
]
