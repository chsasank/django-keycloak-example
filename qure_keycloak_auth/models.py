from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
    """Table of all possible roles.

    :param role: Name of the role
    """
    name = models.CharField(max_length=40, unique=True)
    users = models.ManyToManyField(User, related_name='roles')
