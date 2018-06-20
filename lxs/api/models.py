from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Actor(models.Model):
    ROLES = (
        ('interviewer', 'Interviewer'),
        ('candidate', 'Candidate'),
    )
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=30, choices=ROLES)


class Slot(models.Model):
    WEEKDAYS = (
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
    )
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    weekday = models.CharField(choices=WEEKDAYS, max_length=30)
    start = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(23)])

    class Meta:
        unique_together = ()


class Interview(models.Model):
    candidate = models.ForeignKey(Actor, on_delete=models.CASCADE)
    interviewers = models.ManyToManyField(Actor, related_name='appointments')
    date = models.DateField()
    slot = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(23)])

    class Meta:
        unique_together = (('candidate', 'date', 'slot'),)


