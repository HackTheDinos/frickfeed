from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
import routers.v1 as v1router


urlpatterns = [
    # Base Application
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^v1/', include(v1router.router.urls))
]
