from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse


class Bill(models.Model):
    name = models.CharField(unique=True, max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    due_date = models.DateField()

    def get_absolute_url(self, *args, **kwargs):
        return reverse('bill_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Bill, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Payment(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date_paid = models.DateField()

