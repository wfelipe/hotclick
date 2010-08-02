from django.http import HttpResponse
from hotclick.click.models import *

def process_click(request):
	click = Click()

	for attr in request.GET:
		if hasattr(click, attr):
			setattr(click, attr, request.GET[attr])

	click.save()

	return HttpResponse()
