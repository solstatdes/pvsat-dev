from django.db import models
from django.utils import timezone
from committee.models import Member

class Session(models.Model):
    session = models.CharField(max_length=20)
    start = models.DateTimeField()
    finish = models.DateTimeField()
    chair = models.CharField(max_length=100, null=True, blank=True)


    def __unicode__(self):
        return self.session

class Poster(models.Model):
    session = models.CharField(max_length=20)
    start = models.DateTimeField()
    finish = models.DateTimeField()
    chair = models.CharField(max_length=100, null=True, blank=True)


    def __unicode__(self):
        return self.session
