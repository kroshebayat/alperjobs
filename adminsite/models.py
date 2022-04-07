from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class ExtraFields(models.Model):
    country = models.CharField(max_length=30)
    province = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    userActiveStatus = models.BooleanField(default=False)
    emailConfirmation = models.BooleanField(default=False)
    balance = models.CharField(max_length=100)
    userLevels = (
        ('1', 'Bronze'),
        ('2', 'Silver'),
        ('3', 'Gold'),
    )
    level = models.CharField(max_length=1, choices=userLevels)
    companySizeOptions = (
        ('1', '0-10'),
        ('2', '10-20'),
        ('3', '20-50'),
        ('4', '50-100'),
        ('5', '+100'),
    )
    companyName = models.CharField(max_length=60)
    companySize = models.CharField(max_length=1, choices=companySizeOptions)
    companyEstablished = models.CharField(max_length=4)
    userpositions = (
        ('1', 'employer'),
        ('2', 'candidate'),
    )


class User(AbstractUser):
    phoneNumber = models.CharField(max_length=12)
    exteraField = models.ForeignKey(ExtraFields, on_delete=models.DO_NOTHING)
    email = models.EmailField('email address', unique=True)


class BlogModel(models.Model):
    conditionOfPost = (
        ('1', 'Published'),
        ('2', 'UnPublished'),
        ('3', 'Deleted'),
    )
    title = models.CharField(max_length=300)
    slug = models.CharField(max_length=300)
    description = models.TextField()
    mainPicture = models.ImageField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dateTime = models.DateTimeField()
    condition = models.CharField(max_length=1, choices=conditionOfPost)


class JobPositions(models.Model):
    jobTitle = models.CharField(max_length=200)
    jobCreator = models.ForeignKey(User, on_delete=models.CASCADE)
    jobCreatedDateTime = models.DateTimeField()
    jobExpiration = models.DateField()
    jobDesctiption = models.TextField()
    jobSkils = models.TextField()
    jobAppliedUsers = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_jobAppliedUsers')
    jobAppliedsCounter = models.CharField(max_length=5)
