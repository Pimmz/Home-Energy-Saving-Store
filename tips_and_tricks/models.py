from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone

# Create your models here.


class TipsAndTricks(models.Model):

    title = models.CharField(max_length=200, unique=True, default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField('Content')
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class ApprovalStatus(models.Model):
    post = models.OneToOneField(TipsAndTricks, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
