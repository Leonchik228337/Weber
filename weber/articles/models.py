from datetime import datetime

from django.db import models
from django.utils import timezone


class Article(models.Model):
	title = models.CharField(max_length=200, verbose_name="Заголовок")
	text = models.TextField(verbose_name="Текст")
	time_create = models.DateTimeField(auto_now=datetime.now, verbose_name="Дата создания")
	time_change = models.DateField(auto_now_add=timezone.now, verbose_name="Дата изменения")
	category = models.ForeignKey("Category", on_delete=models.PROTECT, null=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Статья"
		verbose_name_plural = "Статьи"
		ordering = ["title"]


class Category(models.Model):
	name = models.CharField(max_length=50, verbose_name="Название", db_index=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Категория"
		verbose_name_plural = "Категории"
		ordering = ["name"]
