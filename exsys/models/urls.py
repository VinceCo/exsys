from django.conf.urls import url

from models import views

urlpatterns = [
    url(r'^$', views.redirect_home),
    url(r'^home/?$', views.home, name="home_models"),
    url(r'^model/(?P<id_title>[\w\s]+)/?$', views.model, name="model"),
]
