from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'parks.views.home', name='home'),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
]
