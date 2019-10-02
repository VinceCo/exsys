from django.conf.urls import url

from scale import views

urlpatterns = [
    url(r'^$', views.redirect_home),
    url(r'^home/?$', views.home, name="home"),
    url(r'^test/?$', views.test, name="test"),
]
