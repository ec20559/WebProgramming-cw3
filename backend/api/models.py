# backend/api/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)

    # Added related_name argument to avoid clashes with the default User model
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        related_query_name='custom_user',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        related_query_name='custom_user',
        blank=True,
    )

    class Article(models.Model):

        class Status(models.TextChoices):
            DRAFT = 'DF', 'Draft'
            PUBLISHED = 'PB', 'Published'

        author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_articles')
        title = models.CharField(max_length=250)
        slug = models.SlugField(max_length=250)
        body = models.TextField()
        publish = models.DateTimeField(default=timezone.now)
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        status = models.CharField(max_length=2,
                                    choices=Status.choices,
                                    default=Status.DRAFT
                                )


        class Meta:
            ordering = ['-publish']
            indexes = [
                models.Index(fields=['-publish']),
            ]
            pass

        def __str__(self):
            return self.title
            pass

        pass


