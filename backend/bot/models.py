from django.db import models

class BotResponse(models.Model):
    question = models.CharField(max_length=255, default='default_value')
    bot_response = models.TextField()

    def __str__(self):
        return self.question
