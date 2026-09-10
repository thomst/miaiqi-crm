from django.db import models


class StoreType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Store type'
        verbose_name_plural = 'Store types'

    def __str__(self):
        return self.name


class Store(models.Model):
    PENDING = 'pending'
    B2B = 'b2b'
    ON_COMMISSION = 'on-commission'
    NO_INTEREST = 'no-interest'

    STATUS_CHOICES = [
        (PENDING, 'pending'),
        (B2B, 'business to business'),
        (ON_COMMISSION, 'on commission'),
        (NO_INTEREST, 'no interest'),
    ]

    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    street_address = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    website = models.URLField(blank=True)
    type = models.ForeignKey(
        'StoreType',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='stores',
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=PENDING,
    )
    note = models.TextField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Contact(models.Model):
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name='contacts',
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    note = models.TextField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
