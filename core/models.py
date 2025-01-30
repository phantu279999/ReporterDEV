from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


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


class Comment(TimeStampedModel):
	creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='creator')
	content = models.TextField()
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')
