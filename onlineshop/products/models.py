from djongo import models


class Parameter(models.Model):
    uid = models.ObjectIdField()
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)


class Product(models.Model):
    uid = models.ObjectIdField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    params = models.ArrayField(
        model_container=Parameter
    )
