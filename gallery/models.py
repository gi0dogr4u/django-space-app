from datetime import datetime

from django.db import models


class Gallery(models.Model):

    STAR = 1
    GALAXY = 2
    PLANET = 3
    NEBULA = 4
    EARTH = 5
    CATEGORIES = [
        (STAR, 'Star'),
        (GALAXY, 'Galaxy'),
        (PLANET, 'Planet'),
        (NEBULA, 'Nebula'),
        (EARTH, 'Earth')
    ]

    id = models.IntegerField(primary_key=True, editable=False)
    path = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    name = models.CharField(max_length=100)
    legend = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    category = models.IntegerField("Categories of Astronomy Events", choices=CATEGORIES)
    publish = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'

    def __str__(self):
        return f'Photo - {self.name}'

    @staticmethod
    def get_categories():
        return [tag[1] for tag in Gallery.CATEGORIES]
