from django.db import models

# Create your models here.


class Vendor(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    code = models.CharField(max_length=6, blank=False, unique=True, null=False)
    type = models.CharField(max_length=15, blank=False, null=False)


class Invoice(models.Model):
    vendor = models.ForeignKey(
        Vendor,
        related_name="invoice",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    document_number = models.IntegerField(unique=True, null=False, blank=False)
    invoice_numbers = models.IntegerField(null=False, blank=False)
    type = models.CharField(max_length=2, null=False, blank=False)
    doc_date = models.DateField()
    posting_date = models.DateField()
    due_date = models.DateField()
    amount_in_loc = models.IntegerField()
