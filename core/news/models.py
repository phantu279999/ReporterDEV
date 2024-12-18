from django.db import models
from ckeditor.fields import RichTextField

from accounts.models import Author
from core.models import TimeStampedModel

NEWS_TYPE = (
	('normal', 'Normal'),
	('video', 'Video'),
	('image', 'Image'),
)

class Zone(models.Model):
	name = models.CharField(max_length=255, db_index=True)
	meta_name = models.CharField(max_length=255, blank=True)
	meta_keyword = models.CharField(max_length=255, blank=True)
	meta_description = models.CharField(max_length=255, blank=True)
	url = models.SlugField()
	parent_id = models.IntegerField(blank=True)

	def __str__(self):
		return self.name


class Tag(TimeStampedModel):
	name = models.CharField(max_length=255, db_index=True)
	meta_name = models.CharField(max_length=255, blank=True)
	meta_keyword = models.CharField(max_length=255, blank=True)
	meta_description = models.CharField(max_length=255, blank=True)
	url = models.SlugField()

	def __str__(self):
		return self.name


class News(TimeStampedModel):
	title = models.CharField(max_length=255, db_index=True)
	sapo = models.CharField(max_length=255)
	avatar = models.ImageField(upload_to='avatar', blank=True)
	news_type = models.CharField(max_length=100, choices=NEWS_TYPE)
	status = models.BooleanField(default=True)
	slug = models.SlugField(unique=True)
	content = RichTextField(blank=True)

	created_by = models.CharField(max_length=200, blank=True)
	edited_by = models.CharField(max_length=200, blank=True)

	is_on_home = models.BooleanField(default=False)
	is_focus = models.BooleanField(default=False)
	is_pr = models.BooleanField(default=False)

	author = models.ForeignKey(Author, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def word_count(self):
		return 0

	class Meta:
		ordering = ('-created_date',)


class NewsInZone(models.Model):
	zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
	news = models.ForeignKey(News, on_delete=models.CASCADE)

	def __str__(self):
		return "{}->{}".format(self.news.title, self.zone.name)


class TagNews(models.Model):
	tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
	news = models.ForeignKey(News, on_delete=models.CASCADE)

	def __str__(self):
		return "{}->{}".format(self.news.title, self.tag.name)
