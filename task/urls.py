from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('update-task/<str:pkey>',views.Update,name='update'),
    path('delete-task/<str:pkey>',views.Delete,name='delete'),
]