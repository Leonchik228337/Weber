from django.http import HttpResponse
from django.shortcuts import render
from .forms import Login
from django.contrib.auth.models import User


def index(request):
	if request.method == "POST":
		login_form = Login(request.POST)
		if login_form.is_valid():
			context = {"is_register": False}
			username = login_form.cleaned_data["username"]
			password = login_form.cleaned_data["password"]
			user = User.objects.create_user(username=username, password=password)
			user.save()

			return render(request, "index.html", context)
		else:
			return render(request, "reg_error.html", context={"form": login_form})
	else:
		login_form = Login()

		context = {
			"title": "Index",
			"form": login_form,
			}
		return render(request, "login.html", context)


def articles(request):
	context = {"title": "Все статьи"}
	return render(request, "articles/index.html", context)


def about(request):
	context = {"title": "about"}
	return render(request, "articles/about.html", context)


def registration(request):
	reg_form = Login()
	context = {"title": "Регистрация", "form": reg_form}
	return render(request, "registration.html", context)
