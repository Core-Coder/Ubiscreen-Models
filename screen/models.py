from django.db import models

# Choice old way

SIZE_CHOICES = (
    ('1', '40 Inches'),
    ('2', '41 Inches'),
    ('3', '42 Inches'),
    ('4', '43 Inches'),
)

# Create your models here.

# Choice new
class Resolution(models.TextChoices):
    Widescreen_1920x1080 = '16:9'
    Widescreen1_1920x1080 = '16:9_2'
    Widescreen2_1920x1080 = '16:9_3'
    Widescreen3_1920x1080 = '16:9_4'

class MonetizationStatus(models.IntegerChoices):
    On = 1
    Off = 2

class Branch(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.address}'

class Videotron(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    image = models.ImageField(upload_to='videotron_img')
    width = models.IntegerField(verbose_name='Width (in m)')
    height = models.IntegerField(verbose_name='Height (in m)')
    resolution = models.CharField(max_length=100, choices=Resolution.choices)
    address = models.TextField()
    monetization_status = models.IntegerField(default='2', choices=MonetizationStatus.choices)
    monetization_price = models.IntegerField(verbose_name='Monetization Price (per 15s)')

    def __str__(self):
        return f'{self.name}'

    def size(self):
        return f'{self.width}x{self.height}'

class Television(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    image = models.ImageField(upload_to='television_img')
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    size = models.CharField(max_length=100, choices=SIZE_CHOICES)
    resolution = models.CharField(max_length=100, choices=Resolution.choices)
    position = models.CharField(max_length=100)
    monetization_status = models.IntegerField(default='2', choices=MonetizationStatus.choices)
    monetization_price = models.IntegerField(verbose_name='Monetization Price (per 15s)')
    
    def __str__(self):
        return f'{self.name}'