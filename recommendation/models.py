from django.db import models
from django.utils.encoding import smart_text

class WordScore_Manager(models.Manager):
    def create_scoredata(self, word, score):
        data = self.create(
            word=word,
            score=score
        )
        return data

class Hospital_Manager(models.Manager):
    def create_hospitaldata(self, code, name, addr, phone):
        data = self.create(
            code=code,
            name=name,
            addr=addr,
            phone=phone
        )
        return data

class WordScore(models.Model):
    word = models.CharField(max_length=50)
    score = models.DecimalField(max_digits=4, decimal_places=3)
    type = models.CharField(max_length=10)
    # objects = WordScore_Manager()

    def __str__(self):
        return smart_text(self.word) + '：' + smart_text(self.score)

class Hospital(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    addr = models.CharField(max_length=300)
    phone = models.CharField(max_length=100)
    objects = Hospital_Manager()

    def __str__(self):
        return smart_text(self.name)

class HospitalScore(models.Model):
    hospital = models.OneToOneField(Hospital, related_name="hospital_detail")
    total_WOM = models.IntegerField(default=0)

    score_ec = models.DecimalField(max_digits=5, decimal_places=3, default=0)  # Economic
    count_ec = models.IntegerField(default=0)
    score_tem = models.DecimalField(max_digits=5, decimal_places=3, default=0)  # Temporal
    count_tem = models.IntegerField(default=0)
    score_con = models.DecimalField(max_digits=5, decimal_places=3, default=0)  # Convenience
    count_con = models.IntegerField(default=0)
    score_soc = models.DecimalField(max_digits=5, decimal_places=3, default=0)  # Sociopsychological
    count_soc = models.IntegerField(default=0)
    score_qua = models.DecimalField(max_digits=5, decimal_places=3, default=0)  # Quality
    count_qua = models.IntegerField(default=0)
    score_oth = models.DecimalField(max_digits=5, decimal_places=3, default=0)  # Other
    count_oth = models.IntegerField(default=0)

    def __str__(self):
        return smart_text(self.hospital.name) + '：' + smart_text(self.score)
