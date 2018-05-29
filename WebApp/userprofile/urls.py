from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', login, {'template_name': 'userprofile/login.html'})#Between the {} goes your HTML template of what you would like to render on screen. Login.html still needs to be created. Maybe need to include login/ after ^ idk yet
]
