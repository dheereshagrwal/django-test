from django.db import models
from product.models import Product
from django.contrib.auth.models import User

# Create your models here.


class Cart(models.Model):
    cart_id = models.CharField(max_length=250, unique=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        unique_together = ('product', 'cart')

    def sub_total(self):
        return self.product.price * self.quantity