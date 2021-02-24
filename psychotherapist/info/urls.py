from django.urls import path
from . import views

app_name = 'info'
urlpatterns = [
    path('', views.index, name= 'index'),
    path('<str:rec_id>', views.lc, name= 'lc'),
]