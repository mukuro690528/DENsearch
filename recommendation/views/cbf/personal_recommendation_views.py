from recommendation.views.cbf import base
from django.shortcuts import render

def PersonalRecommendation(request):
    if request.method == "POST":
        q1 = request.POST['q1']
        q2 = request.POST['q2']
        q3 = request.POST['q3']
        q4 = request.POST['q4']
        q5 = request.POST['q5']
        q6 = request.POST['q6']

        print(q1 + ' , ' + q2 + ' , ' + q3 + ' , ' + q4 + ' , ' + q5 + ' , ' + q6)

    return render(request, 'result.html')

def CountScore():
    pref = [4, 3, 4, 2, 5, 5]
    print(pref)


if __name__ == '__main__':
    CountScore()