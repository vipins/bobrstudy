from django.conf.urls import patterns, include, url
from survey import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myapp.views.home', name='home'),
    # url(r'^myapp/', include('myapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
	#url(r'^', views.name),
	#url(r'^recd/', views.name_recd),
	url(r'^start/', views.serve),
	url(r'^submission/', views.process_submission),
)
