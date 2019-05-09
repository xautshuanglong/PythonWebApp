from django.db import models


class UserInfo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    sex = models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        return "{ " + self.id + ", " + self.name + " }"
