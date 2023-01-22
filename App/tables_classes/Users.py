from App import models
import datetime

class Users:


    @staticmethod
    def add(name, surname, email):
        item = models.Users(name=name, surname=surname, email=email, date=datetime.date.today())
        item.save()


    @staticmethod
    def get():
        return models.Users.objects.all()