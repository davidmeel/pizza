from django.db import models

# Create your models here.


class MainScrollModel(models.Model):
    title = models.CharField(max_length=50)
    info = models.CharField(max_length=255)
    discount = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to='main-scroll')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'scroll'
        verbose_name_plural = 'scrolls'



class Menu(models.Model):
    image = models.ImageField(upload_to='menu')
    title = models.CharField(max_length=50)
    info = models.CharField(max_length=64)
    price = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'menu'
        verbose_name_plural = 'menues'