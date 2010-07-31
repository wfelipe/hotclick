from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^', 'hotclick.click.views.process_click'),
)
