from django.db import models

# Create your models here.


class TextImporter(models.Model):
    sales_order = models.IntegerField(unique=True)
    posting_period = models.IntegerField()
    fiscal_year = models.IntegerField()
    customer = models.IntegerField()
    bill_document = models.IntegerField()



