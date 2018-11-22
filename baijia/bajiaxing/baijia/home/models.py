from django.db import models


class Name(models.Model):

    name = models.CharField(max_length=512)
    usename = models.CharField(max_length=512)

    class Meta:
        db_table = 'baijiaxing'
