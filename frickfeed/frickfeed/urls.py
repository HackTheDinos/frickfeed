from django.conf.urls import include, url
from django.contrib import admin
from apps.records.views import IndexView
import routers.v1 as v1router


urlpatterns = [
    url(r'^$', IndexView),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^v1/', include(v1router.router.urls))
]
