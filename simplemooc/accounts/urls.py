from django.conf.urls import url
from django.contrib.auth.views import login as authLogin
from simplemooc.accounts.views import register

urlpatterns = [
    url(r'^$', authLogin, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^cadastrar/', register, name='register'),
     
]