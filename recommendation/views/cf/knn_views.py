from recommendation.views import base
import math
from recommendation.models import UserData


def create_trainset():
    """
    產生訓練集合。
    :return:
    """
    trainset_tf = dict()
    user_data = UserData.objects.all()
    for user in user_data:
        trainset_tf[user.id] = (
            user.pre1, user.pre2, user.pre3, user.pre4, user.pre5, user.ena1, user.ena2, user.ena3, user.need1,
            user.need2, user.need3, user.service1, user.service2, user.service3)

    return trainset_tf

def cosine_similarity(v1, v2):
    """
    計算兩個向量的正弦相似度。距離越近，相似度數值會越高。
    :param v1:
    :param v2:
    :return:
    """
    sum_xx, sum_xy, sum_yy = 0.0, 0.0, 0.0
    for i in range(0, len(v1)):
        sum_xx += math.pow(v1[i], 2)
        sum_xy += v1[i] * v2[i]
        sum_yy += math.pow(v2[i], 2)

    return sum_xy / math.sqrt(sum_xx * sum_yy)

def knn_classify(input_tf, k):
    tf_distance = dict()
    # 計算每個訓練集合特徵關鍵字字詞頻率向量和輸入向量的距離
    trainset_tf = create_trainset()

    # (1) 計算向量距離
    for place in trainset_tf.keys():
        tf_distance[place] = cosine_similarity(trainset_tf.get(place), input_tf)

    # 把距離排序，取出k個最近距離的分類
    # (2) 取K個最近鄰居的分類
    sim_user = []
    for i, place in enumerate(sorted(tf_distance, key=tf_distance.get, reverse=True)):
        sim_user.append(str(place))
        if (i + 1) >= k:
            break

    return sim_user

if __name__ == '__main__':
    input_tf = (1, 2, 1, 2, 2, 3, 1, 3, 2, 1, 1, 2, 1, 2)
    sim_user = knn_classify(input_tf, k=5)
