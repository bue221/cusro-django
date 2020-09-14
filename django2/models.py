from django.db import models

# Create your models here.

class Articulo(models.Model):
    title = models.CharField(max_length=150)
    img = models.ImageField(default='null', upload_to="articulos")
    content = models.TextField()
    public = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Categoria(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    created_at = models.DateField()

