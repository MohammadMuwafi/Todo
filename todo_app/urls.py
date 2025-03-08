from importlib.resources import path
from django.urls import path
from . import views


app_name = 'todo_app'


urlpatterns = [
    path("", views.TodoList.as_view(), name="home"),
    path("<int:pk>/read", views.TodoDetail.as_view(), name="todo_detail"),
    path("<int:pk>/update", views.TodoUpdate.as_view(), name="todo_update"),
    path("<int:pk>/delete", views.DeleteView.as_view(), name="todo_delete"),
    path("create", views.TodoCreate.as_view(), name="todo_create"),
    
    path("delete_all_todos", views.details_for_delete_all_todos, name="details_for_delete_all_todos"),
    path("delete_todos/", views.delete_all_todos, name="delete_all_todos"),
    path("search_todo/", views.search_todo, name="search_todo"),
]
