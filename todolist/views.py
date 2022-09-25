from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from todolist.models import Task
from todolist.forms import TaskForm


@login_required(login_url="/todolist/login/")
def show_todolist(request):
    user = request.user
    todolist = Task.objects.filter(user=user)
    return render(
        request,
        template_name="todolist.html",
        context={
            "todolist": todolist,
            "username": user.username,
        },
    )


@login_required(login_url="/todolist/login/")
def create_task(request):
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            user = request.user
            data = form.cleaned_data
            Task.objects.create(user=user, **data)
            return HttpResponseRedirect(reverse("todolist:show_todolist"))

    return render(request, "create-task.html", {"form": form})


@login_required(login_url="/todolist/login/")
def update_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    is_finished = not task.is_finished
    task.is_finished = is_finished
    task.save()
    return redirect("todolist:show_todolist")


@login_required(login_url="/todolist/login/")
def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return redirect("todolist:show_todolist")


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Akun telah berhasil dibuat!")
            return redirect("todolist:login")

    context = {"form": form}
    return render(request, "register.html", context)


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("todolist:show_todolist")
        else:
            messages.info(request, "Username atau Password salah!")

    context = {}
    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    return redirect("todolist:login")
