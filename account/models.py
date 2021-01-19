from django.db import models


# Create your models here.


class Account(models.Model):
    name = models.CharField(max_length=30, verbose_name=u"机构名称", unique=True)
    balance = models.FloatField(default=0.0, verbose_name=u"余额")

    class Meta:
        verbose_name = "组"


