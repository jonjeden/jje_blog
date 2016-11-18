from django import forms

from .models import Post, Comment, Task, TaskNote, Contact, ContactNote

class PostForm(forms.ModelForm):
	
	#which model to create a form for, and which fields exposed
	class Meta:
		model = Post
		fields = ('title', 'text',)
		
class CommentForm(forms.ModelForm):
	
	class Meta:
		model = Comment
		fields = ('author', 'text',)

class TaskNoteForm(forms.ModelForm):
	
	class Meta:
		model = TaskNote
		fields = ('note_author', 'note',)
		
class ContactForm(forms.ModelForm):
	
	class Meta:
		model = Contact
		fields = ('first_name', 'last_name', 'email', 'phone1',)
		
class ContactNoteForm(forms.ModelForm):
	
	class Meta:
		model = ContactNote
		fields = ('note_author', 'note',)