from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.CoursesView.as_view(), name='courses'),
	url(r'^diary/$', views.DiaryView.as_view(), name='diary'),
	url(r'^course(?P<pk>[0-9]+)/$', views.CourseView.as_view(), name='course'),
	url(r'^instance(?P<pk>[0-9]+)/$', views.InstanceView.as_view(), name='instance'),
]