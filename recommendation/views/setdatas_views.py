from recommendation.models import *
import csv
import os

# set word score data
def get_WordScoredata(request):  # set word score data
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
