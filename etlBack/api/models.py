from django.db import models


class Transaction(models.Model):
    transactionID = models.CharField(
        primary_key=True, max_length=100, default=0)
    date = models.DateTimeField(default="")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    merchantName = models.CharField(max_length=100, blank=True, null=True)


class TransformationBlock(models.Model):
    operation = models.CharField(max_length=100)
    percentage = models.DecimalField(max_digits=10, decimal_places=2)
    label = models.CharField(max_length=100)
