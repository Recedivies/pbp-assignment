from django.urls import path
from todolist.views import (
    register,
    login_user,
    logout_user,
    show_todolist,
    create_task,
    update_task,
    delete_task,
    show_todolist_json,
    add_task_ajax,
)

app_name = "todolist"

urlpatterns = [
    path("", show_todolist, name="show_todolist"),
    path("create-task/", create_task, name="create-task"),
    path("update/<int:pk>/", update_task, name="update-task"),
    path("delete/<int:pk>/", delete_task, name="delete-task"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("json/", show_todolist_json, name="show_todolist_json"),
    path("add/", add_task_ajax, name="add_task_ajax"),
]
