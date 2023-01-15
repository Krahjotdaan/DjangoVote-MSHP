from App import models
import datetime

class Answer_Users:
    def create_user_answer(self, description, voting_id):
        item = Answer_Users(description=description, voting_id=voting_id)
        item.save()

    def read_user_answer(self):
        return Answer_Users.objects.all()
