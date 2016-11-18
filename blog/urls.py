from django.conf.urls import url, include, patterns
from blog import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^project/$', views.project_list, name='project_list'),
	url(r'^project/(?P<pk>\d+)/$', views.project_detail, name='project_detail'),
	#
	url(r'^contact/$', views.contact_list, name='contact_list'),
	url(r'^contact/(?P<pk>\d+)/$', views.contact_detail, name='contact_detail'),
	url(r'^contact/new/$', views.contact_new, name='contact_new'),
    url(r'^contact/(?P<pk>\d+)/edit/$', views.contact_edit, name='contact_edit'),
    url(r'^contact/(?P<pk>\d+)/contactnote/$', views.add_note_to_contact, name='add_contact_note'),
    #
	url(r'^task/$', views.task_list, name='task_list'),
	url(r'^task/(?P<pk>\d+)/$', views.task_detail, name='task_detail'),
	url(r'^task/(?P<pk>\d+)/tasknote/$', views.add_note_to_task, name='add_task_note'),
    #
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    #
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    #url(r'^search/$', views.search_post_list, name='search_blog_posts'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
]
