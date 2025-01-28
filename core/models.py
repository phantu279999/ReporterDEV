from django.db import models

# Abstract class base
class TimeStampedModel(models.Model):
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)
	published_at = models.DateTimeField(blank=True, null=True, db_index=True)

	class Meta:
		abstract = True


class CommonNewsModel(models.Model):
	title = models.CharField(max_length=255, db_index=True)
	sapo = models.CharField(max_length=255)
	slug = models.SlugField(unique=True, db_index=True)
	created_by = models.CharField(max_length=200, blank=True)
	edited_by = models.CharField(max_length=200, blank=True)

	class Meta:
		abstract = True