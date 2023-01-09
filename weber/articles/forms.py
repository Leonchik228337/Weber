from django import forms


class Registration(forms.Form):
	email = forms.RegexField(max_length=100, label="Электронная почта", widget=forms.EmailInput(),
	                         regex=r"^[a-zA-Z0-9А-ЯА-Я]+@[a-zA-ZА-ЯА-Я]+\.[a-zA-ZА-ЯА-Я]+$")
	password = forms.RegexField(widget=forms.PasswordInput(), regex=r"^\w+$", label="Пароль")
	field_order = ["email", "password"]
