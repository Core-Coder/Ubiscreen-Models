from django.db import models
from media.models import Playlist
from screen.models import Videotron, Television
from multiselectfield import MultiSelectField
from django.utils.timezone import now

# Create your models here.

class Schedule(models.Model):
    DAY_CHOICES = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )

    class DateChoices(models.TextChoices):
        ALLTIME = 'All Time'
        CUSTOM = 'Custom'

    class HourChoices(models.TextChoices):
        ALLDAY = 'All Day'
        CUSTOM = 'Custom'

    class StatusChoices(models.TextChoices):
        ON = 'On'
        OFF = 'Off'

    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=3, default='Off', verbose_name="Status (Auto)", choices=StatusChoices.choices)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    date_option = models.CharField(max_length=10, choices=DateChoices.choices)
    start_date = models.DateField(default=now, verbose_name='Start Date (if Date Option is Custom)')
    end_date = models.DateField(default=now, verbose_name='End Date (if Date Option is Custom)')
    day = MultiSelectField(choices=DAY_CHOICES)
    hour_option = models.CharField(max_length=10, choices=DateChoices.choices)
    start_hour = models.TimeField(default=now, verbose_name='Start Hour (if Hour Option is Custom)')
    end_hour = models.TimeField(default=now, verbose_name='End Hour (if Hour Option is Custom)')
    videotrons = models.ManyToManyField(Videotron)
    televisions = models.ManyToManyField(Television)
    date_created = models.DateField(auto_now_add=True)

    def total_screen(self):
        total = self.videotrons.count() + self.televisions.count()
        return total