from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^metabolite_details/', views.metabolite_details, name='metabolite_details'),
]