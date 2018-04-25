from recommendation.views import base
from .knn_views import knn_classify
from recommendation.models import UserData, UserLike


def CFrecommendation(input_tf):
    sim_user = knn_classify(input_tf, 5)
    new_user = UserData(pre1=input_tf[0], pre2=input_tf[1], pre3=input_tf[2], pre4=input_tf[3], pre5=input_tf[4],
                        ena1=input_tf[5], ena2=input_tf[6], ena3=input_tf[7], need1=input_tf[8], need2=input_tf[9],
                        need3=input_tf[10], service1=input_tf[11], service2=input_tf[12], service3=input_tf[13])
    new_user.save()

    cf_list = {}
    for u in sim_user:
        user_like = UserLike.objects.filter(user=u)
        for h in user_like:
            if h.hospital.name in cf_list:
                cf_list[h.hospital.name] += 1
            else:
                cf_list[h.hospital.name] = 1

    return cf_list


