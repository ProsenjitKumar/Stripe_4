from django.db import models


class ProductCategory(models.Model):
    title = models.CharField(max_length=44)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=55)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    price = models.IntegerField()
    image = models.ImageField(upload_to='photo/', blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name

