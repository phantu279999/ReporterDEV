from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUserManager(BaseUserManager):
	groups = models.ManyToManyField(
		Group,
		related_name="customuser_set",  # Add a unique related_name
		blank=True,
	)
	user_permissions = models.ManyToManyField(
		Permission,
		related_name="customuser_set",  # Add a unique related_name
		blank=True,
	)
	def create_user(self, email, password=None, **extra_fields):
		if not email:
			raise ValueError("The Email field must be set")
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user


	def create_superuser(self, email, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError("Superuser must have is_staff=True.")
		if extra_fields.get('is_superuser') is not True:
			raise ValueError("Superuser must have is_superuser=True.")

		return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
	class Types(models.TextChoices):
		ADMIN = 'admin', 'Admin'
		AUTHOR = 'author', 'Author'
		READER = 'reader', 'Reader'

	base_type = Types.READER
	user_type = models.CharField(_("Type"), max_length=10, choices=Types.choices, default=Types.READER)
	email = models.EmailField(unique=True)
	username = None

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['user_type']

	objects = CustomUserManager()


class AuthorManager(BaseUserManager):
	def get_queryset(self, *args, **kwargs):
		return super().get_queryset(*args, **kwargs).filter(user_type=CustomUser.Types.AUTHOR)


# Proxy model
class Author(CustomUser):
	base_type = CustomUser.Types.AUTHOR
	objects = AuthorManager()

	class Meta:
		proxy = True


class ReaderManager(BaseUserManager):
	def get_queryset(self, *args, **kwargs):
		return super().get_queryset(*args, **kwargs).filter(user_type=CustomUser.Types.READER)


class Reader(CustomUser):
	base_type = CustomUser.Types.READER
	objects = ReaderManager()

	class Meta:
		proxy = True


class AuthorProfile(models.Model):
	user = models.OneToOneField(Author, on_delete=models.CASCADE)
	full_name = models.CharField(max_length=50, blank=True)
	avatar = models.ImageField(upload_to='avatar_user', blank=True)
	bio = models.CharField(max_length=255, blank=True)
	phone = models.CharField(max_length=11, blank=True)
	address = models.CharField(max_length=50, blank=True)

	link_facebook = models.CharField(max_length=100, blank=True)
	link_x = models.CharField(max_length=100, blank=True)
	link_other = models.CharField(max_length=100, blank=True)

	def __str__(self):
		return self.user.email


@receiver(post_save, sender=Author)
def create_author_profile(sender, instance, created, **kwargs):
	if created:
		AuthorProfile.objects.create(user=instance)


@receiver(post_save, sender=Author)
def save_author_profile(sender, instance, **kwargs):
	instance.authorprofile.save()
