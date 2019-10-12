from django.conf.urls import url

from scale import views

urlpatterns = [
    url(r'^$', views.redirect_home),
    url(r'^home/?$', views.home, name="home"),
    url(r'^energy/?$', views.energy, name="energy"),
    url(r'^machine/?$', views.machine, name="machine"),
    url(r'^machine_power/?$', views.machine_power, name="machine_power"),
    url(r'^machine_consumption/?$', views.machine_consumption, name="machine_consumption"),
]
