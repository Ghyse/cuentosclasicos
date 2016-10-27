from django.conf.urls import include, url
from django.contrib import admin
from cuento import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('cuento.urls')),  
    url(r'^cuento/(?P<pk>[0-9]+)/$', views.show_cuento),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
