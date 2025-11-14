from django.db import models

class Portfolio(models.Model):
    user = models.CharField(max_length=100)
    stock_symbol = models.CharField(max_length=10)
    quantity = models.IntegerField()
    purchase_price = models.FloatField()
    purchase_date = models.DateField(auto_now_add=True)
