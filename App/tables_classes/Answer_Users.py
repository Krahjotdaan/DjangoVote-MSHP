from App import models
import datetime

class Answer_Users:
    @staticmethod
    def create(description, voting_id):
        item = Answer_Users(description=description, voting_id=voting_id)
        item.save()

    @staticmethod
    def read():
        return Answer_Users.objects.all()
