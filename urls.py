from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='evaluate-index'),
    url(r'^evaluate/', views.evaluate_workshop, name='evaluate-workshop'),
    url(r'^view/', views.view, name='evaluate-view')
]