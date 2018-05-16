from recommendation.views import base
from django.shortcuts import render
from recommendation.views.cbf.cbf_recommendation_views import CountScore
from recommendation.views.cf.cf_recommendation_views import CFrecommendation
from recommendation.models import Hospital, UserLike, UserData


def PersonalRecommendation(request):
    if request.method == "POST":
        q1 = request.POST['q1']
        q2 = request.POST['q2']
        q3 = request.POST['q3']
        q4 = request.POST['q4']
        q5 = request.POST['q5']
        q6 = request.POST['q6']

        pre1 = request.POST['pre1']
        pre2 = request.POST['pre2']
        pre3 = request.POST['pre3']
        pre4 = request.POST['pre4']
        pre5 = request.POST['pre5']

        ena1 = request.POST['ena1']
        ena2 = request.POST['ena2']
        ena3 = request.POST['ena3']

        need1 = request.POST['need1']
        need2 = request.POST['need2']
        need3 = request.POST['need3']

        service1 = request.POST['service1']
        service2 = request.POST['service2']
        service3 = request.POST['service3']

        input_data = (
            int(pre1), int(pre2), int(pre3), int(pre4), int(pre5), int(ena1), int(ena2), int(ena3), int(need1),
            int(need2), int(need3), int(service1), int(service2), int(service3))

        # 協同過濾式推薦
        cf_list = CFrecommendation(input_data)

        # 內容式推薦 + 混合
        rank_cbf = CountScore(q1, q2, q3, q4, q5, q6, 5, cf_list)

    return render(request, 'result.html', {'rank': rank_cbf})


def SetUserLike(request):
    if request.method == "POST":
        r1 = request.POST['r1']
        r2 = request.POST['r2']
        r3 = request.POST['r3']
        r4 = request.POST['r4']
        r5 = request.POST['r5']
        UserLikeToDB(r1, r2, r3, r4, r5)

        # print(r1 + ' , ' + r2 + ' , ' + r3 + ' , ' + r4 + ' , ' + r5)

    return render(request, 'thankyou.html')

def UserLikeToDB(r1, r2, r3, r4, r5):
    s1 = r1.split('.')
    s2 = r2.split('.')
    s3 = r3.split('.')
    s4 = r4.split('.')
    s5 = r5.split('.')
    all_data = [s1, s2, s3, s4, s5]
    user = UserData.objects.order_by('id').last()
    for d in all_data:
        if int(d[0]) > 4:
            hospital = Hospital.objects.get(name=d[1])
            user_like = UserLike(user=user, hospital=hospital)
            user_like.save()

if __name__ == '__main__':
    UserLikeToDB("4.冠眾牙醫診所", "2.聯安牙醫診所", "2.百齡牙醫診所", "4.上揚牙醫診所", "4.龍安牙醫診所")