from django import forms


class Registration(forms.Form):
	username = forms.RegexField(max_length=100, regex=r"^[A-Za-z0-9А-Яа-я_-]+$",
	                            help_text="Пароль не может содержать специальные символы")

	password = forms.RegexField(widget=forms.PasswordInput(), regex=r"^\w+$", min_length=8,
	                            help_text="Минимальная длина пароля 8 символов, пароль не может содержать \
	                             специальные символы")
	field_order = ["username", "password"]
