from django.db import models
from django.utils import timezone
from s3direct.fields import S3DirectField

from django.utils.text import slugify
from time import time
import transliterate
from django.contrib.auth.models import User


def gen_slug(s):
    for i in s:
        if i.lower() in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            new_slug = transliterate.translit(slugify(s, allow_unicode=True), reversed=True)
            if Post.objects.filter(slug__iexact=new_slug).count():
                return new_slug + '-' + str(int(time()))
            return new_slug
    new_slug = slugify(s)
    if Post.objects.filter(slug__iexact=new_slug).count():
        return new_slug + '-' + str(int(time()))
    return new_slug


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True, blank=True)
    body = models.TextField(blank=True, db_index=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #image = models.ImageField(default='default.jpg', upload_to='post_pics')
    image =S3DirectField(dest='post_destination')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-date_posted',)


class Review(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True, blank=True)
    body = models.TextField(blank=True, db_index=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image =S3DirectField(dest='review_destination')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-date_posted',)
