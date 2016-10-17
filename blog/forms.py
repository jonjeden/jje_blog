from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):
	
	#which model to create a form for, and which fields exposed
	class Meta:
		model = Post
		fields = ('title', 'text',)
		
class CommentForm(forms.ModelForm):
	
	class Meta:
		model = Comment
		fields = ('author', 'text',)
