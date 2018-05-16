from recommendation.views import base
from recommendation.models import HospitalScore
from operator import itemgetter

# 內容式推薦分數計算
def CountScore(q1, q2, q3, q4, q5, q6, c, cf_list):
    pref = [int(q1), int(q2), int(q3), int(q4), int(q5), int(q6)]
    hospital = HospitalScore.objects.all()
    rank = []
    rank_c = []
    # print(cf_list)
    for h in hospital:
        p_score = h.score_ec * pref[0] + h.score_tem * pref[1] + h.score_con * pref[2] + h.score_soc * pref[
            3] + h.score_qua * pref[4] + h.score_oth * pref[5]
        for l in cf_list:
            if h.hospital.name == l:
                p_score = p_score + 10 * cf_list[l]
        if p_score != 0:
            rank.append((h.hospital.name, p_score, h.total_WOM))


    rank.sort(key=itemgetter(1, 2), reverse=True)
    for i in range(c):
        # print(rank[i][0] + '：' + str(rank[i][1]))
        # s = round(((rank[i][1] - rank[c+1][1]) / (rank[0][1] - rank[c+1][1])) * 10, 2)
        s = round((rank[i][1] / rank[0][1]) * 10, 2)
        rank_c.append((rank[i][0], str(s)))

    return rank_c


if __name__ == '__main__':
    CountScore(1, 1, 1, 1, 1)