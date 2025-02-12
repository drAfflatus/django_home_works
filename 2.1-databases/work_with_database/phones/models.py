from django.db import models


class Phone(models.Model):

    # TODO: Добавьте требуемые поля

    # id, name, price, image, release_date, lte_exists и slug
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80, null=False)
    image = models.URLField(default=None)
    price = models.IntegerField(default=None)
    release_date = models.DateField(default=None)
    lte_exists = models.BooleanField(default=None)
    slug = models.SlugField(default=None)



