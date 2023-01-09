from django.http import HttpResponse
from django.shortcuts import render
from .forms import Registration


def index(request):
	if request.method == "POST":
		reg_form = Registration(request.POST)
		if reg_form.is_valid():
			email = reg_form.cleaned_data["email"]
			password = reg_form.cleaned_data["password"]
			context = {
				"email": email,
				"password": password,
				}
			return render(request, "index.html", context)
		else:
			reg_form.email.initial = reg_form.cleaned_data["email"]
			reg_form.password.initial = reg_form.cleaned_data["password"]
			return render(request, "reg_error.html")
	else:
		reg_form = Registration()

		context = {
			"title": "Index",
			"form": reg_form,
			}
		return render(request, "login.html", context)


def articles(request):
	context = {
		"title": "Все статьи",
		}
	return render(request, "articles/index.html", context)


def about(request):
	context = {
		"title": "about",
		}
	return render(request, "articles/about.html", context)
