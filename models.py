from django.db import models

# Create your models here.

class QuestionnaireResponse(models.Model):
    user_id = models.CharField(max_length=255)
    phq9_score = models.IntegerField()
    gad7_score = models.IntegerField()
