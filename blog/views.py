from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment, Task, TaskNote, Project, Department, Contact, ContactNote
from .forms import PostForm, CommentForm, TaskNoteForm, ContactForm, ContactNoteForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.mail import send_mail

#Create your views here.
#view for blog posts (main page)
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})

#view to show list of current IT projects
def project_list(request):
	projects = Project.objects.filter(visible=True).order_by('name')
	return render(request, 'project/project_list.html', {'projects': projects})

#view to show list of current tasks
@login_required
def task_list(request):
	tasks = Task.objects.all()
	return render(request, 'task/task_list.html', {'tasks': tasks})

#contacts/leads!
@login_required
def contact_list(request):
	contacts = Contact.objects.all().order_by('first_name')
	return render(request, 'contact/contact_list.html', {'contacts': contacts})


#detailed view for given contact
@login_required
def contact_detail(request, pk):
	contact = get_object_or_404(Contact, pk=pk)
	return render(request, 'contact/contact_detail.html', {'contact': contact})

#detailed view for given project
def project_detail(request, pk):
	project = get_object_or_404(Project, pk=pk)
	return render(request, 'project/project_detail.html', {'project': project})

#function to get task objects from database - called in base html file as a context object
@login_required
def get_task_list():
	task_list = Task.objects.all()
	return task_list

#show details about a task
@login_required
def task_detail(request, pk):
	task = get_object_or_404(Task, pk=pk)
	return render(request, 'task/task_detail.html', {'task': task})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})
	
#basic search through blog posts
def search_post_list(request, search_query):
	posts = Post.objects.filter(Q(intro__icontains=search_query)).order_by('-published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def post_new(request):
	#handle blank form and a filled out blog form/post that was submitted
	#if we send post data to this view (post method from form on website), 
	#we must create a new post, save, then redirect.
	#else this is a new post with no data. 
	if request.method == "POST": 
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})
	
#view to edit a post - pass in PK for this view to edit a specific post
#then pass post in as instance
@login_required
def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})
	
#view to post drafts of unpublished blog posts
@login_required
def post_draft_list(request):
	posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
	return render(request, 'blog/post_draft_list.html', {'posts': posts})
	
#view to publish a blog post!
@login_required
def post_publish(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.publish()
	return redirect('post_detail', pk=pk)

#view to delete a blog post
@login_required
def post_remove(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.delete()
	return redirect('post_list')
	
def add_comment_to_post(request, pk):
	#get post (if exists) first
	post = get_object_or_404(Post, pk=pk)
	#if submitting a comment, do the following:
	if request.method == "POST":
		form = CommentForm(request.POST) #get comment form
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = CommentForm() #not posting, but blank form on load
	return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
	comment = get_object_or_404(Comment, pk=pk)
	comment.approve()
	return redirect('post_detail', pk=comment.post.pk)
	
@login_required
def comment_remove(request, pk):
	comment = get_object_or_404(request, pk)
	post_pk = comment.post.pk
	comment.delete()
	return redirect('post_detail', pk=post_pk)

@login_required
def contact_edit(request, pk):
	contact = get_object_or_404(Contact, pk=pk)
	if request.method == "POST":
		form = ContactForm(request.POST, instance=contact)
		if form.is_valid():
			contact = form.save(commit=False)
			contact.save()
			return redirect('contact_detail', pk=contact.pk)
	else:
		form = ContactForm(instance=contact)
	return render(request, 'contact/contact_edit.html', {'form': form})

#view for creating new contact
@login_required
def contact_new(request):
	if request.method == "POST": 
		form = ContactForm(request.POST)
		if form.is_valid():
			contact = form.save(commit=False)
			contact.save()
			return redirect('contact_detail', pk=contact.pk)
	else:
		form = ContactForm()
	return render(request, 'contact/contact_edit.html', {'form': form})

#add a simple note to a task
@login_required
def add_note_to_task(request, pk):
	#get note if it exists, first
	task = get_object_or_404(Task, pk=pk)
	#if submitting a note, do the following:
	if request.method == "POST":
		form = TaskNoteForm(request.POST) #get note form
		if form.is_valid():
			task_note = form.save(commit=False)
			task_note.post = post
			task_note.save()
			return redirect('tasknote_detail', pk=post.pk)
	else:
		form = TaskNoteForm() #not posting, but blank form on load
	return render(request, 'blog/add_task_note.html', {'form': form})

#add a simple note to a contact and then send email
@login_required
def add_note_to_contact(request, pk):
	contact = get_object_or_404(Contact, pk=pk)
	#if submitting a note, do the following:
	if request.method == "POST":
		form = ContactNoteForm(request.POST) #get note form
		if form.is_valid():
			contact_note = form.save(commit=False)
			contact_note.contact = contact
			contact_note.save()
			#subject, body, from email, to email, fail?
			message = "Contact " + contact.first_name + " " + contact.last_name + " was updated with new note: " + contact_note.__str__()
			send_mail('Contact note added', message, 'BigJ@scorcher.pythonanywhere.com', ['jonjeden@gmail.com'], fail_silently=False) 
			return redirect('contact_list')
	else:
		form = ContactNoteForm() #not posting, but blank form on load
	return render(request, 'contact/add_contact_note.html', {'form': form, 'contact': contact})