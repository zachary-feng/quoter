from django.conf.urls import url
from . import views

app_name = 'feed'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^submit/$', views.submit, name='submit')
]