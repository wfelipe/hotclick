from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Example:
	# (r'^hotclick/', include('hotclick.foo.urls')),

	# Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
	# to INSTALLED_APPS to enable admin documentation:
	# (r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	(r'^admin/', include(admin.site.urls)),

	# click
	(r'^click/', include('hotclick.click.urls')),
	# reports
	(r'^reports/', include('hotclick.reports.urls')),
	# heat
	(r'^heat/', include('hotclick.heat.urls')),
)
