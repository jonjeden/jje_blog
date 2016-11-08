from django.db import models
from django.utils import timezone
from django.forms.fields import URLField
import datetime

PRIORITY_CHOICES = (
				(1, 'Low'),
				(2, 'Normal'),
				(3, 'High'),
				)

# Create your models here.
class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200) #limited length
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	
	#method to actually post the new draft post. When you create a post,
	#it isn't auto published (a good thing).
	def publish(self):
		self.published_date = timezone.now()
		self.save()
		
	def approved_comments(self):
		return self.comments.filter(approved_comment=True)
		
	def __str__(self):
		return self.title
		
class Comment(models.Model):
	#related name allows us to have access comments from a Post model
	post = models.ForeignKey('blog.Post', related_name='comments')
	author = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	approved_comment = models.BooleanField(default=False)
	
	#method to allow/show a user comment. must be approved.
	def approve(self):
		self.approved_comment = True
		self.save()
		
	def __str__(self):
		return self.text

#tasks or events that are upcoming
class Task(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	author = models.ForeignKey('auth.User')
	due_date = models.DateTimeField(blank=True, null=True)
	created_date = models.DateTimeField(default=timezone.now)
	completed = models.BooleanField(default=False)
	priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
	
	def mdy_due_date(self):	
		str_date = self.due_date.strftime("%b") + ' ' + self.due_date.day.__str__()
		return str_date
	
	class Meta:
		ordering = ['-priority', 'title']
	
	class Admin:
		pass
	
	def __str__(self):
		return self.title

#note related to a task
class TaskNote(models.Model):
	task = models.ForeignKey('blog.Task', related_name='task_notes')
	note = models.CharField(max_length=400)
	note_author = models.ForeignKey('auth.User')
	created_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.note

		
class WebLink(models.Model):
	title = models.CharField(max_length=200)
	web_url = models.URLField(max_length=400, blank=True)
	
	class Meta:
		ordering = ['title', 'web_url']
	
	def __str__(self):
		return self.title

'''
Project that is being followed by subscribers
and tracked with notes. the notes help generate emails
    
class Project(models.Model):
    name = models.CharField(max_length=200, unique=True)
    number = models.IntegerField(default=0)
    department = models.ForeignKey(Department) #FK
    description = models.CharField(max_length=400, blank=True)
    fiscal_year = models.IntegerField(default=0)
    total_cost = models.FloatField(max_length=40, default=0)
    start_date = models.DateField(default="2000-01-01")
    #close_date = models.DateField()
    last_update = models.DateTimeField(auto_now=True)
    visible = models.BooleanField(default=True)
    
    #subscribers = models.ManyToManyField('Subscriber', blank=True)
    
    def __str__(self): 
        return self.name
    
    class Meta:
        ordering = ('name',)
'''
"""
#this defines typically a government department that a project falls under
class Department(models.Model):
    name = models.CharField(max_length=200, unique=True)
    staff_size = models.IntegerField(default=0)
    budget = models.FloatField(default=0)
    website = models.URLField(blank=True)
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=2, blank=True)
    zipcode = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

	def budget(self):
		return "$%s" % self.budget

    class Meta:
        ordering = ('name',)

"""
