from django.shortcuts import render
from todo_app.models import Todo
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
import logging

# Create a logger instance
logger = logging.getLogger(__name__)

class TodoList(ListView):
    model = Todo
    context_object_name = "todo_list"
    
    def get_queryset(self):
        logger.debug("TodoList view accessed.")
        return super().get_queryset()

class TodoDetail(DetailView):
    model = Todo
    
    def get_object(self, queryset=None):
        todo = super().get_object(queryset)
        logger.debug(f"Accessed Todo details for: {todo.title}")
        return todo

class TodoCreate(CreateView):
    model = Todo
    fields = "__all__"
    success_url = reverse_lazy("todo_app:home")

    def form_valid(self, form):
        logger.info(f"Todo created: {form.instance.title}")
        return super().form_valid(form)

class TodoUpdate(UpdateView):
    model = Todo
    fields = "__all__"
    success_url = reverse_lazy("todo_app:home")

    def form_valid(self, form):
        logger.info(f"Todo updated: {form.instance.title}")
        return super().form_valid(form)

class DeleteView(DeleteView):
    model = Todo
    fields = "__all__"
    success_url = reverse_lazy("todo_app:home")

    def delete(self, request, *args, **kwargs):
        todo = self.get_object()
        logger.info(f"Todo deleted: {todo.title}")
        return super().delete(request, *args, **kwargs)

def details_for_delete_all_todos(request):
    logger.debug("User visited the delete all todos confirmation page.")
    return render(request, 'todo_app/details_for_delete_all_todos.html')

def delete_all_todos(request):
    logger.info("All Todos are being deleted.")
    Todo.objects.all().delete()
    return HttpResponseRedirect(reverse('todo_app:home'))

def search_todo(request):
    search_value = request.GET.get('search-bar', '')
    logger.debug(f"Search for todos with title containing: {search_value}")
    context = {
        "todo_list": Todo.objects.all().filter(title__contains=search_value)
    }
    return render(request, "todo_app/todo_list.html", context)
