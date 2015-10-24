"""hhealth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from default_app import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.dashboard), # default
    url(r'^login/$', views.login_user),

    url(r'^api/case/all$', views.api_case_all),
    url(r'^api/case/update$', views.api_case_update),
    url(r'^api/case/delete/([a-zA-Z0-9]+)/$', views.api_case_delete),
    url(r'^api/candidate/all$', views.api_candidate_all),
    url(r'^api/candidate/update$', views.api_candidate_update),
    url(r'^api/candidate/delete/([a-zA-Z0-9]+)/$', views.api_candidate_delete),
    url(r'^api/examiner/all$', views.api_examiner_all),
    url(r'^api/examiner/update$', views.api_examiner_update),
    url(r'^api/examiner/delete/([a-zA-Z0-9]+)/$', views.api_examiner_delete),
    url(r'^api/venue/all$', views.api_venue_all),
    url(r'^api/venue/update$', views.api_venue_update),
    url(r'^api/venue/delete/([a-zA-Z0-9]+)/$', views.api_venue_delete),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)