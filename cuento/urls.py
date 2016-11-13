from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.show_main_cuentos),
 	url(r'^cuento/(?P<pk>[0-9]+)/$', views.show_cuento, name='cuento'),
]