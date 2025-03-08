from django.shortcuts import render
from todo_app.models import Todo
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView


class TodoList(ListView):
    model = Todo
    context_object_name = "todo_list"


class TodoDetail(DetailView):
    model = Todo


class TodoCreate(CreateView):
    model = Todo
    fields = "__all__"
    success_url = reverse_lazy("todo_app:home")


class TodoUpdate(UpdateView):
    model = Todo
    fields = "__all__"
    success_url = reverse_lazy("todo_app:home")


class DeleteView(DeleteView):
    model = Todo
    fields = "__all__"
    success_url = reverse_lazy("todo_app:home")


def details_for_delete_all_todos(request):
    return render(request, 'todo_app/details_for_delete_all_todos.html')


def delete_all_todos(request):
    Todo.objects.all().delete()
    return HttpResponseRedirect(reverse('todo_app:home'))


def search_todo(request):
    search_value = request.GET['search-bar']
    # for exact title ==> Todo.objects.all().filter(title=search_value),
    context = {
        "todo_list": Todo.objects.all().filter(title__contains=search_value)
    }
    return render(request, "todo_app/todo_list.html", context)


# def order_by(request):
#     if request.GET['field'] not in ["id", "title"]:
#         return HttpResponseRedirect(reverse('todo_app:home'))
#     if request.GET['field'] == "Todo ID":
#         value = "pk"
#     elif request.GET['field'] == "Todo title":
#         value = "title"
#     else:
#         value = "?"
#     context = {
#         "todo_list": Todo.objects.order_by(value)
#     }
#     print(Todo.objects.order_by(value))
#     return render(request, "todo_app/todo_list.html", context)
