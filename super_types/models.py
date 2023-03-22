from django.db import models


# Create your models here.


class SuperType(models.Model):
    """this is a super type model """
    type = models.CharField(max_length=250)


class Super(models.Model):
    """this is a supermodel """
    name = models.CharField(max_length=250)
    alter_ego = models.CharField(max_length=250)
    primary_ability = models.CharField(max_length=250)
    secondary_ability = models.CharField(max_length=250)
    catchphrase = models.CharField(max_length=250)
    super_type = models.ForeignKey(SuperType, on_delete=models.CASCADE)
