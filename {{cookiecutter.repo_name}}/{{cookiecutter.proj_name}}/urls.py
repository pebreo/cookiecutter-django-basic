from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cookiecutter_proj_name.views.home', name='home'),
    # url(r'^cookiecutter_proj_name/', include('cookiecutter_proj_name.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    url(r'^{{cookiecutter.app_name}}/', include('{{cookiecutter.app_name}}.urls', namespace='{{cookiecutter.app_name}}')),
    
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
