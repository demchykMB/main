from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, db_column=True)
    slug = models.SlugField(max_length=100, unique=True)


    class Meta:
        ordering = 'name'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категирии'

    def __str__(self):
       return self.name


class Produkt(models.Model):
    category = models.ForeignKey(Category, related_name='produkt', on_delete=models.CASCADE())
    name = models.CharField(max_length=100, db_column=True)
    slug = models.CharField(max_length=100, db_column=True)




