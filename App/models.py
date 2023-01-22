from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Voting(models.Model):
    """
    Таблица голосований
    """
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(to=User, default=1, on_delete=models.CASCADE)  # связь 1:N


class VoteVariant(models.Model):
    """
    Таблица вариантов ответов
    """
    description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now)
    voting_id = models.ForeignKey(to=Voting, on_delete=models.CASCADE)  # связь 1:N


class VoteFact(models.Model):
    """
    Таблица ответов пользователей
    """
    author = models.ForeignKey(to=User, default=1, on_delete=models.CASCADE)  # связь 1:N
    variant = models.ForeignKey(to=VoteVariant, default=1, on_delete=models.CASCADE)  # связь 1:N
    created_at = models.DateTimeField(default=timezone.now)
