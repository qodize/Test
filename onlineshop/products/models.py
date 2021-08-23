from djongo import models


class Parameter(models.Model):
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    class Meta:
        abstract = True


class Product(models.Model):
    uid = models.ObjectIdField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    params = models.ArrayField(
        model_container=Parameter
    )
