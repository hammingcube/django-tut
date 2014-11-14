from django.conf.urls import patterns, url
from polls import views


urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/results/5/
    url(r'^results/(?P<question_id>\d+)/$', views.detail, name='alt'),
)