from django.db import models


class Users(models.Model): # таблица пользователи
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.EmailField()
    date = models.DateTimeField()


class Voting(models.Model): # таблица голосований
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    date = models.DateTimeField(default=0)
    author = models.ForeignKey(to=Users, blank=True, null=True, on_delete=models.SET_NULL) # связь 1:N


class Answer_Choise(models.Model): # таблица вариантов ответов
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=1000)
    date = models.DateTimeField(default=0)
    voting_id = models.ForeignKey(to=Users, blank=True, null=True, on_delete=models.SET_NULL) # связь 1:NS


class Answer_Users(models.Model): # таблица ответов пользователей
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=1000)
    author = models.ManyToManyField(Users, blank=True) # связь M:N
    voting_id = models.ManyToManyField(Voting, blank=True) # связь M:N

