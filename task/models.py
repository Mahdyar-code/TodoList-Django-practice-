from _pyrepl.completing_reader import complete
from django.utils import timezone

from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField()
    high = 1
    medium = 2
    low = 3
    priority_status  = (
        (high, 'High'),
        (medium, 'Medium'),
        (low, 'Low')
    )
    priority = models.IntegerField(choices=priority_status, default=high)
    completed = 1
    in_progress = 2
    status_choices = (
        (in_progress, 'In progress'),
        (completed, 'Completed')
    )
    state = models.IntegerField(choices=status_choices, default=in_progress)

    def __str__(self):
        return self.title

