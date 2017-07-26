from django.conf.urls import url
from simplemooc.core.views import home
from simplemooc.core.views import contato
from simplemooc.core.views import index


urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^contato/', contato, name='contato'),
]