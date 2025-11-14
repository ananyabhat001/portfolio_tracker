from django.db import models

class Stock(models.Model):
    user = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    quantity = models.PositiveIntegerField()
    purchase_price = models.FloatField()

    def __str__(self):
        return f"{self.symbol} ({self.user})"
