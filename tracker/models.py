from django.db import models
from datetime import timedelta


class Period(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    notes = models.TextField(blank=True)

    @property
    def period_length(self):
        return (self.end_date - self.start_date).days + 1

    @property
    def next_period_date(self):
        return self.start_date + timedelta(days=28)

    def __str__(self):
        return self.name