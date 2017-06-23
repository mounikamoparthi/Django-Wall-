from django.conf.urls import url
from . import views          
urlpatterns = [
    url(r'^$', views.index, name = 'my_index'),
    url(r'^register$', views.registration, name = 'my_registration'),
    url(r'^login$', views.loginuser, name = 'my_loginuser')
  ]