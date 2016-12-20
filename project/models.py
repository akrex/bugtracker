from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Topic(models.Model):
    name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=30, null=True, unique=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse('project:project', args=[str(self.pk)])

    def __str__(self):
        return self.name


class Issue(models.Model):
    tittle = models.CharField(max_length=200)
    comment = models.CharField(max_length=2000)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.SET(1))
    topic = models.ForeignKey(Topic, on_delete=models.SET(1))
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField()

    def get_absolute_url(self):
        return reverse('project:issue', args=[str(self.project_id), str(self.pk)])


class IssueComment(models.Model):
    comment = models.CharField(max_length=2000)
    created = models.DateTimeField()
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('project:issue', args=[str(self.issue.project_id), str(self.issue_id)])


