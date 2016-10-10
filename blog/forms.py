from django import forms

from .models import Post

class PostForm(forms.ModelForm):
	
	#which model to create a form for, and which fields exposed
	class Meta:
		model = Post
		fields = ('title', 'text',)
