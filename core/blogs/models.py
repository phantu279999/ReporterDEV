from django.db import models
from ckeditor.fields import RichTextField

from accounts.models import Author
from core.models import TimeStampedModel

from common.common import count_word, get_reading_time


class Category(models.Model):
	name = models.CharField(max_length=255, db_index=True)
	meta_name = models.CharField(max_length=255, blank=True)
	meta_keyword = models.CharField(max_length=255, blank=True)
	meta_description = models.CharField(max_length=255, blank=True)
	url = models.SlugField()

	def __str__(self):
		return self.name


class Blog(TimeStampedModel):
	title = models.CharField(max_length=255, db_index=True)
	sapo = models.CharField(max_length=255)
	avatar = models.ImageField(upload_to='avatar_blog', blank=True)
	status = models.BooleanField(default=True)
	slug = models.SlugField(unique=True, db_index=True)
	content = RichTextField(blank=True)

	created_by = models.CharField(max_length=200, blank=True)
	edited_by = models.CharField(max_length=200, blank=True)

	is_on_home = models.BooleanField(default=False)
	is_focus = models.BooleanField(default=False)

	author = models.ForeignKey(Author, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def word_count(self):
		return count_word(self.content)

	def reading_time(self):
		return get_reading_time(self.word_count())

	class Meta:
		ordering = ('-created_date',)


class BlogInCate(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

	def __str__(self):
		return "{}->{}".format(self.blog.title, self.category.name)
