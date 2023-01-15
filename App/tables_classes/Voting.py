from App import models
import datetime

class Voting:
    @staticmethod
    def add(title, description, author):
        item = models.Voting(title=title, description=description, date=datetime.date.today(), author=author)
        item.save()


    @staticmethod
    def get():
        return models.Voting.objects.all()