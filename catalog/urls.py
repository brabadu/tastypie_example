from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from app.api import CabinetResource

cabinet_resource = CabinetResource()


urlpatterns = patterns('',
    # url(r'^catalog/', include('catalog.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(cabinet_resource.urls))
)
