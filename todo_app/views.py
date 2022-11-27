from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView, CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import TodoItem
from .forms import TodoItemCreateForm, TodoItemUpdateForm
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse_lazy


class HomeView(View):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        context = {
            'home': True
        }
        return render(request, self.template_name, context)


class TaskItemsListView(LoginRequiredMixin, ListView):
    model = TodoItem
    queryset = TodoItem.objects.all()
    template_name = "todo/todo_list.html"
    context_object_name = "tasks_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = True
        return context

    def get_queryset(self):
        return TodoItem.objects.filter(user=self.request.user,archive=False)


class TaskItemArchivedListView(TaskItemsListView):
    def get_queryset(self):
        return TodoItem.objects.filter(user=self.request.user,archive=True)

class TaskItemCreateView(LoginRequiredMixin, CreateView):
    form_class = TodoItemCreateForm
    model = TodoItem
    template_name = "todo/task_create.html"

    def form_valid(self, form):
        task = form.save(commit=False)
        task.user = self.request.user
        task.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self) -> str:
        return reverse_lazy("todo_app:tasks")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create'] = True 
        return context


class TaskItemUpdateView(LoginRequiredMixin, UpdateView):
    form_class = TodoItemUpdateForm
    model = TodoItem
    pk_url_kwarg = "pk"
    template_name = "todo/task_create.html"
    success_url = reverse_lazy("todo_app:tasks")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not obj.user == self.request.user:
            raise Http404
        return obj


class TaskItemDeleteView(LoginRequiredMixin, View):
    success_url = reverse_lazy("todo_app:tasks")

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(
            TodoItem, pk=kwargs.get("pk"), user=request.user)
        obj.delete()
        return HttpResponseRedirect(self.success_url)


class TaskItemDetailView(LoginRequiredMixin, DetailView):
    model = TodoItem
    template_name = "todo/todo_detail.html"
    context_object_name = "task"
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise Http404
        return obj
