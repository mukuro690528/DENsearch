from recommendation.models import *
import csv
import os

# set word score data
def get_WordScoredata(request):
    workpath = os.path.dirname(os.path.join(os.path.dirname("__file__"), os.path.pardir))
    c = os.path.join(workpath, 'static/dataset/wordScore.csv')
    with open(c, "r", encoding='big5', errors='ignore') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            WordScore.objects.create_scoredata(
                row['word'],
                row['score']
            )
    return reader

# set hospital and score data
def get_Hospitaldata(request):
    workpath = os.path.dirname(os.path.join(os.path.dirname("__file__"), os.path.pardir))
    c = os.path.join(workpath, 'static/dataset/all1061117.csv')
    with open(c, "r", encoding='big5', errors='ignore') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            tmp = Hospital.objects.create_hospitaldata(
                row['code'],
                row['name'],
                row['address'],
                row['phone']
            )
            hospitalScore = HospitalScore(hospital=tmp, score=0)
            hospitalScore.save()

    return reader
