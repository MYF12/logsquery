from  django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^query1$', views.query1, name='query1'),
    url(r'^queryresult1$', views.queryresult1, name='queryresult1'),
    # url(r'^queryresult2$', views.queryresult2, name='queryresult2'),
    url(r'logsnewcontent$', views.logsnewcontent, name='logsnewcontent'),
    url(r'logsnewcontent1$', views.logsnewcontent1, name='logsnewcontent1'),
    url(r'logsformat$', views.logsformat, name='logsformat'),
    url(r'logsformatForm$', views.logsformatForm, name='logsformatForm'),
    url(r'^downfile/$', views.downfile,name='downfile'),
]