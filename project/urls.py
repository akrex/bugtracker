"""bugtracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

app_name = "project"

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^my/$', views.MyProjectView.as_view(), name='my-projects'),
    url(r'^(?P<pk>[0-9]+)/$', views.ProjectView.as_view(), name='project'),
    url(r'^add/$', views.ProjectAddView.as_view(), name='project-add'),
    url(r'^about/$', views.ProjectAboutView.as_view(), name='about'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.ProjectUpdateView.as_view(), name='project-update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.ProjectDeleteView.as_view(), name='project-delete'),
    url(r'^(?P<project_id>[0-9]+)/issue/(?P<pk>[0-9]+)/$', views.IssueView.as_view(), name='issue'),
    url(r'^(?P<project_id>[0-9]+)/issue/add/$', views.IssueAddView.as_view(), name='issue-add'),
    url(r'^(?P<project_id>[0-9]+)/issue/(?P<pk>[0-9]+)/update/$', views.IssueUpdateView.as_view(), name='issue-update'),
    url(r'^(?P<project_id>[0-9]+)/issue/(?P<pk>[0-9]+)/delete/$', views.IssueDeleteView.as_view(), name='issue-delete'),
    url(r'^(?P<project_id>[0-9]+)/issue/(?P<issue_id>[0-9]+)/comment/add$', views.IssueCommentAddView.as_view(),
        name='issue-comment-add'),
    url(r'^(?P<project_id>[0-9]+)/issue/(?P<issue_id>[0-9]+)/comment/update/(?P<pk>[0-9]+)/$',
        views.IssueCommentUpdateView.as_view(), name='issue-comment-update'),
    url(r'^(?P<project_id>[0-9]+)/issue/(?P<issue_id>[0-9]+)/comment/delete/(?P<pk>[0-9]+)/$',
        views.IssueCommentDeleteView.as_view(), name='issue-comment-delete'),
]
