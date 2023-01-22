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


    @staticmethod
    def update():
        user_id = models.Users.id
        users = models.Users.objects.filter(id=user_id)
        users.name = models.Users.name
        users.surname = models.Users.surname
        users.email = models.Users.email
        users.save()


    @staticmethod
    def delete():
        user_id = models.Users.id
        users = models.Users.objects.filter(id=user_id)
        users.delete()
