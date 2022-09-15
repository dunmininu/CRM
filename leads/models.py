from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

# Create your models here.


class User(AbstractUser):
    is_organiser = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    agent = models.ForeignKey(
        "Agent",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    category = models.ForeignKey(
        "Category",
        related_name="leads",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    description = models.TextField()
    date_added = models.DateField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class Category(models.Model):
    # New, contacted, converted, unconverted
    name = models.CharField(max_length=30)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)
