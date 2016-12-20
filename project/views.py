import datetime
from django.shortcuts import redirect
from django.views import generic
from .models import Project, Issue, IssueComment
from django.core.urlresolvers import reverse_lazy
from django.urls import reverse


def login_check(funct):
    def func_wrapper(obj, *args, **kwargs):
        if obj.request.user.id is None:
            return redirect('user:login')
        return funct(obj, *args, **kwargs)
    return func_wrapper



class IndexView(generic.ListView):
    template_name = 'project/index.html'
    context_object_name = 'all_projects'

    def get_queryset(self):
        return Project.objects.all()


class ProjectView(generic.DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'project/project.html'


class ProjectAddView(generic.CreateView):
    model = Project
    fields = ['name', 'url']

    @login_check
    def dispatch(self, *args, **kwargs):
        return super(ProjectAddView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.owner_id = self.request.user.id
        return super(ProjectAddView, self).form_valid(form)


class ProjectUpdateView(generic.UpdateView):
    model = Project
    fields = ['name']

    @login_check
    def dispatch(self, *args, **kwargs):
        return super(ProjectUpdateView, self).dispatch(*args, **kwargs)


class ProjectDeleteView(generic.DeleteView):
    fields = ['name', 'owner']
    model = Project
    success_url = reverse_lazy('user:index')

    @login_check
    def dispatch(self, *args, **kwargs):
        return super(ProjectDeleteView, self).dispatch(*args, **kwargs)


class IssueView(generic.DetailView):
    model = Issue
    context_object_name = 'issue'
    template_name = 'project/issue.html'


class IssueAddView(generic.CreateView):
    model = Issue
    initial = {'topic': 1}
    fields = ['tittle', 'comment', 'topic']

    @login_check
    def dispatch(self, *args, **kwargs):
        return super(IssueAddView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.project_id = self.kwargs['project_id']
        form.instance.owner_id = self.request.user.id
        form.instance.status_id = 1
        form.instance.created = datetime.datetime.now()
        return super(IssueAddView, self).form_valid(form)


class IssueUpdateView(generic.UpdateView):
    model = Issue
    fields = ['status', 'comment']

    @login_check
    def dispatch(self, *args, **kwargs):
        return super(IssueUpdateView, self).dispatch(*args, **kwargs)


class IssueDeleteView(generic.DeleteView):
    model = Issue

    @login_check
    def dispatch(self, *args, **kwargs):
        return super(IssueDeleteView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('project:project', args=[str(self.kwargs['project_id'])])


class IssueCommentAddView(generic.CreateView):
    model = IssueComment
    fields = ['comment']

    @login_check
    def dispatch(self, *args, **kwargs):
        return super(IssueCommentAddView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.issue_id = self.kwargs['issue_id']
        form.instance.owner_id = self.request.user.id
        form.instance.created = datetime.datetime.now()
        return super(IssueCommentAddView, self).form_valid(form)


class IssueCommentUpdateView(generic.UpdateView):
    model = IssueComment
    fields = ['comment']

    @login_check
    def dispatch(self, *args, **kwargs):
        return super(IssueCommentUpdateView, self).dispatch(*args, **kwargs)


class IssueCommentDeleteView(generic.DeleteView):
    model = IssueComment

    @login_check
    def dispatch(self, *args, **kwargs):
        return super(IssueCommentDeleteView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('project:issue', args=[str(self.kwargs['project_id']), str(self.kwargs['issue_id'])])


class ProjectAboutView(generic.TemplateView):
    template_name = 'project/about.html'