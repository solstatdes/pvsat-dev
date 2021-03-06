from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
    url(r'^register/$', 'authors.views.register', name='register'),
    url(r'^login/$', 'authors.views.user_login', name='author-login'),
    url(r'^logout/$', 'authors.views.user_logout', name='author-logout'),
    url(r'^dashboard/$', 'authors.views.dashboard', name='dashboard'),
    url(r'^submit_abstract/', 'authors.views.submit_abstract', name='submit_abstract'),
    url(r'^submit_poster/(?P<abstract_id>\d+)$', 'authors.views.submit_poster', name='submit_poster'),
    url(r'^submit_paper/(?P<abstract_id>\d+)$', 'authors.views.submit_paper', name='submit_paper'),
    url(r'^submit_slides/(?P<abstract_id>\d+)$', 'authors.views.submit_slides', name='submit_slides'),
    url(r'^update_profile/$', 'authors.views.update_profile', name='update_profile'),
)


