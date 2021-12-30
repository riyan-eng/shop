from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(default="category_name", max_length=255)
    def __str__(self):
        return self.category_name

class Condition(models.Model):
    condition_name = models.CharField(default="condition_name", max_length=255)
    def __str__(self):
        return self.condition_name

class Product(models.Model):
    product_name = models.CharField(default="product_name", max_length=255)
    product_category_name = models.ForeignKey("main.Category", on_delete=models.CASCADE)
    product_price = models.DecimalField(max_digits=7, decimal_places=2)
    product_condition = models.ForeignKey("main.Condition", on_delete=models.CASCADE)
    product_minimum_order = models.IntegerField()
    product_description = models.TextField()
    product_created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product_name