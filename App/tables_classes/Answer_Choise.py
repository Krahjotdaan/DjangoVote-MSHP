from App import models
import datetime


class Answer_Choise:
    @staticmethod
    def add(id, description, voting_id):
        item = models.Answer_Choise(id=id, description=description, date=datetime.date.today(), voting_id=voting_id)
        item.save()

    @staticmethod
    def get():
        return models.Answer_Choise.objects.all()
