from django.conf.urls import url
from django.contrib.auth.views import login as authLogin

urlpatterns = [
    url(r'^$', authLogin, {'template_name': 'accounts/login.html'}, name='login'),
     
]