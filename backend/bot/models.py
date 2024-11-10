from django.db import models
from users.models import User
class BotResponse(models.Model):
    question_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=255, default='default_value')
    bot_response = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='botresponse')
    def __str__(self):
        return self.question
