from django.conf.urls import url

from train import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
