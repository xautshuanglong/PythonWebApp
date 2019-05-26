from django.db import models


class UserInfo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    sex = models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        return "{ " + self.id + ", " + self.name + " }"


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
