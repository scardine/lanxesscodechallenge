from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.datastructures import OrderedSet


class Actor(models.Model):
    ROLES = (
        ('interviewer', 'Interviewer'),
        ('candidate', 'Candidate'),
    )
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=30, choices=ROLES)

    @property
    def slots(self):
        return OrderedSet(self.slot_set.order_by('weekday', 'start').values_list('weekday', 'start'))

    @slots.setter
    def slots(self, new_slots):
        current = set(self.slots)
        for weekday, start in current ^ set(new_slots):
            if (weekday, start) in current:
                Slot.objects.get(actor=self, weekday=weekday, start=start).delete()
            else:
                Slot.objects.create(actor=self, weekday=weekday, start=start)

    def __unicode__(self):
        return self.name


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
        unique_together = ('actor', 'weekday', 'start')


class Interview(models.Model):
    candidate = models.ForeignKey(Actor, on_delete=models.CASCADE)
    interviewers = models.ManyToManyField(Actor, related_name='appointments')
    date = models.DateField()
    slot = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(23)])

    class Meta:
        unique_together = (('candidate', 'date', 'slot'),)


