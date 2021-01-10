from django.db import models


class Upload(models.Model):
    customer = models.CharField(max_length=160)
    item = models.CharField(max_length=160)
    total = models.PositiveIntegerField(max_length=100)
    quantity = models.PositiveIntegerField(max_length=100)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.customer} {self.quantity} {self.item}"

