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



class ReservationModel(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    message = models.TextField()
    date = models.CharField(max_length=10)
    time = models.CharField(max_length=15)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'reservation'
        verbose_name_plural = 'reservations'



class GalleryModel(models.Model):
    image = models.ImageField(upload_to="gallery")

    class Meta:
        verbose_name = 'gallery'
        verbose_name_plural = 'galleries'