from django import forms


class ContactForm(forms.Form):

    SUBJECT_CHOICES = (
        (1, 'Return'),
        (2, 'Item Not Delivered'),
        (3, 'Other'),
    )

    name = forms.CharField(label='Your Name')
    email = forms.CharField(label='Your email')
    order_number = forms.CharField(label='Order Number')
    reason_for_contact = forms.ChoiceField(choices=SUBJECT_CHOICES, label='Reason for contact')
