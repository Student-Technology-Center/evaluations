from django.conf.urls import url, include
from . import views
from evaluations.views import evalindex

urlpatterns = [
    url(r'^$', evalindex, name='evalindex'),
    url(r'^evaluate/', views.evaluate_workshop, name='evaluate-workshop'),
    url(r'^thanks/', views.thanks, name='evaluate-thanks'),
]