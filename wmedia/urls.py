from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^wines/$', views.WineListView.as_view(), name='wines'),
	url(r'^wines/(?P<pk>\d+)$', views.WineDetailView.as_view(), name='wine-detail'),
	url(r'^company/$', views.CompanyListView.as_view(), name='company'),
	url(r'^company/(?P<pk>\d+)$', views.CompanyDetailView.as_view(), name='company-detail'),
	url(r'^mywines/$', views.MyWineByUserListView.as_view(), name='MyWine'),
]