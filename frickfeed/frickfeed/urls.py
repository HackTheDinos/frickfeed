from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
import routers.v1 as v1router
from apps.records.views import FacebookLogin


urlpatterns = [
    # Base Application
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^transcribe/', TemplateView.as_view(template_name='transcribe.html')),
    url(r'^v1/', include(v1router.router.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login')
]
