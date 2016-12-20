from django.contrib import admin
from .models import *

admin.site.register(Topic)
admin.site.register(Status)
admin.site.register(Project)
admin.site.register(Issue)
admin.site.register(IssueComment)
