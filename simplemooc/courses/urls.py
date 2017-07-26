from django.conf.urls import url
from simplemooc.courses.views import courses
from simplemooc.courses.views import details

urlpatterns = [
	url(r'^$', courses, name='index'),
	url(r'^(?P<slug>[\w_-]+)/$', details, name='details'),

]