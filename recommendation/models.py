from django.db import models
from django.utils.encoding import smart_text

class WordScore_Manager(models.Manager):
    def create_scoredata(self, word, score):
        data = self.create(
            word=word,
            score=score
        )
        return data

class WordScore(models.Model):
    word = models.CharField(max_length=50)
    score = models.DecimalField(max_digits=4, decimal_places=3)
    objects = WordScore_Manager()

    def __str__(self):
        return smart_text(self.word) + '：' + smart_text(self.score)