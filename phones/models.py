from django.db import models
from django.utils.text import slugify


class Phone(models.Model):

    id = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=200)
    image = models.ImageField()
    price = models.CharField(max_length=50)
    release_date = models.CharField(max_length=50)
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)




