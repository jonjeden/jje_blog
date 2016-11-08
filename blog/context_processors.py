from .models import Task, WebLink
from django.utils import timezone
from django import template

register = template.Library()

# Create your custom context processors here.

#function to get task objects from database
def sidebar(request):
	task_list = Task.objects.all()
	link_list = WebLink.objects.all()
	return {'TASK_LIST': task_list, 'LINK_LIST': link_list}