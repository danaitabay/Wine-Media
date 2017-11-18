from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^wines/$', views.WineListView.as_view(), name='wines'),
	url(r'^wine/(?P<pk>\d+)$', views.WineDetailView.as_view(), name='wine-detail'),
]