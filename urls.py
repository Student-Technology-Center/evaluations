from django.conf.urls import url

import evaluations.views

urlpatterns = [
    url(r'^$', evaluations.views.index, name='index')
]