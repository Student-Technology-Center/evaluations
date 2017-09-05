from django.conf.urls import url, include
from . import views
from evaluations.views import evalindex

urlpatterns = [
    url(r'^$', evalindex, name='evalindex')
]
