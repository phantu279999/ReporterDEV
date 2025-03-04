from django.db import models
from django.db.models import UniqueConstraint
from django.contrib.contenttypes.fields import GenericRelation
from django.db.models import F
from ckeditor.fields import RichTextField

from .tasks import noti_email
from accounts.models import Author, Follow
from core.models import TimeStampedModel, Comment

from common.common import count_word, get_reading_time

NEWS_TYPE = (
	('normal', 'Normal'),
	('video', 'Video'),
	('image', 'Image'),
)

REACT_NEWS = (
	('like', 'Like'),
	('dislike', 'Dislike'),
	('heart', 'Heart'),
	('wow', 'Wow')
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
	slug = models.SlugField(unique=True, db_index=True)
	content = RichTextField(blank=True)
	view_count = models.IntegerField(default=0)

	created_by = models.CharField(max_length=200, blank=True)
	edited_by = models.CharField(max_length=200, blank=True)

	is_on_home = models.BooleanField(default=False)
	is_focus = models.BooleanField(default=False)
	is_pr = models.BooleanField(default=False)

	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	comments = GenericRelation(Comment)

	# Meta SEO
	meta_name = models.CharField(max_length=255, blank=True)
	meta_keyword = models.CharField(max_length=255, blank=True)
	meta_description = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return self.title

	def word_count(self):
		return count_word(self.content)

	def reading_time(self):
		return get_reading_time(self.word_count())

	def increase_view_count(self):
		News.objects.filter(id=self.id).update(view_count=F('view_count') + 1)

	class Meta:
		ordering = ('-created_date',)

	def save(self, *args, **kwargs):
		super(News, self).save(*args, **kwargs)

		followers = Follow.objects.filter(following=self.author).select_related('follower').all()
		for f in followers:
			# print("=============================")
			# print(f.follower.email)
			noti_email.delay(f.follower.email, self.author.email)


class NewsInZone(models.Model):
	zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
	news = models.ForeignKey(News, on_delete=models.CASCADE)

	class Meta:
		constraints = [
			UniqueConstraint(fields=['zone', 'news'], name='unique_zone_news')
		]

	def __str__(self):
		return "{}->{}".format(self.news.title, self.zone.name)


class TagNews(models.Model):
	tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
	news = models.ForeignKey(News, on_delete=models.CASCADE)

	class Meta:
		constraints = [
			UniqueConstraint(fields=['tag', 'news'], name='unique_tag_news')
		]

	def __str__(self):
		return "{}->{}".format(self.news.title, self.tag.name)


class ReactNews(models.Model):
	react = models.CharField(max_length=20, choices=REACT_NEWS)
	news = models.ForeignKey(News, on_delete=models.CASCADE)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)

	class Meta:
		constraints = [
			UniqueConstraint(fields=['author', 'news'], name='unique_author_news')
		]

	def __str__(self):
		return "{} - {} > {}".format(self.author, self.react, self.news.title)
