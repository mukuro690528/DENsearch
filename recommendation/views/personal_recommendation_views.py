from django.shortcuts import render
from recommendation.views.cbf.cbf_recommendation_views import CountScore


def PersonalRecommendation(request):
    if request.method == "POST":
        q1 = request.POST['q1']
        q2 = request.POST['q2']
        q3 = request.POST['q3']
        q4 = request.POST['q4']
        q5 = request.POST['q5']
        q6 = request.POST['q6']

        print(q1 + ' , ' + q2 + ' , ' + q3 + ' , ' + q4 + ' , ' + q5 + ' , ' + q6)
        # 內容式推薦
        rank = CountScore(q1, q2, q3, q4, q5, q6)

    return render(request, 'result.html', {'rank': rank})
