from django.db import models


class Contact(models.Model):

    SUBJECT_CHOICES = (
        ('Return', 'Return'),
        ('Item Not Delivered', 'Item Not Delivered'),
        ('Other', 'Other'),
    )

    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=256, null=False, blank=False)
    order_number = models.CharField(max_length=32, null=True, blank=True)
    subject = models.CharField(
        choices=SUBJECT_CHOICES, max_length=25, null=False, blank=False
    )
    reason_for_contact = models.TextField( 
        null=False, blank=False
    )

    def __str__(self):
        return self.email
