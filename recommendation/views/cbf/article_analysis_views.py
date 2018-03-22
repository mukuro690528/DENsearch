from recommendation.views.cbf import base
import os, csv
import jieba
import jieba.analyse
from recommendation.models import Hospital, HospitalComment, WordScore, HospitalScore

# 將文章分類到各家診所
def ArticalClassification():
    workpath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    c = os.path.join(workpath, '../static/dataset/pttWOM_Taoyuan.csv')
    u_d = os.path.join(workpath, '../static/jiebadict/userdict.txt')
    idf_d = os.path.join(workpath, '../static/jiebadict/idfuserdict.txt')

    jieba.load_userdict(u_d)
    jieba.analyse.set_idf_path(idf_d)

    with open(c, "r", encoding='big5', errors='ignore') as csvfile:
        reader = csv.DictReader(csvfile)
        # count = 0
        for row in reader:
            # t = 0
            sentence = row['content']
            print("Input：", sentence)
            tags = jieba.analyse.extract_tags(sentence, topK=10, withWeight=False)
            for tag in tags:
                a = Hospital.objects.filter(name__startswith=tag)
                if a.exists():
                    print(a[0])
                    HospitalComment.objects.create(hospital_id=a[0].id, content=sentence)


# 分析口碑文章，建立診所分數
def HospitalScore():
    workpath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    u_d = os.path.join(workpath, '../static/jiebadict/userdict.txt')
    idf_d = os.path.join(workpath, '../static/jiebadict/idfuserdict.txt')

    jieba.load_userdict(u_d)
    jieba.analyse.set_idf_path(idf_d)

    hospital = Hospital.objects.all()
    for h in hospital:
        total_artical = 0
        h_dict = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}
        comments = HospitalComment.objects.filter(hospital_id=h.id)

        for c in comments:
            t = 0
            c_score = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}
            c_count = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}
            sentence = c.content
            tags = jieba.analyse.extract_tags(sentence, topK=15, withWeight=False)
            for tag in tags:
                word = WordScore.objects.filter(word=tag)
                if word.exists():
                    c_score[word[0].type] = c_score[word[0].type] + word[0].score
                    c_count[word[0].type] = c_count[word[0].type] + 1
                    if t == 0:
                        total_artical = total_artical + 1
                        t = 1

            for i in range(6):
                if c_count[str(i + 1)] > 0:
                    h_dict[str(i + 1)] = h_dict[str(i + 1)] + (c_score[str(i + 1)] / c_count[str(i + 1)])

        h.hospital_score.total_WOM = total_artical
        if total_artical > 0:
            h.hospital_score.score_ec = round(h_dict['1'] / total_artical, 4)
            h.hospital_score.score_tem = round(h_dict['2'] / total_artical, 4)
            h.hospital_score.score_con = round(h_dict['3'] / total_artical, 4)
            h.hospital_score.score_soc = round(h_dict['4'] / total_artical, 4)
            h.hospital_score.score_qua = round(h_dict['5'] / total_artical, 4)
            h.hospital_score.score_oth = round(h_dict['6'] / total_artical, 4)
        h.hospital_score.save()

        print(str(h.hospital_score.score_ec) + ',' + str(h.hospital_score.score_tem) + ',' +
              str(h.hospital_score.score_con) + ',' + str(h.hospital_score.score_soc) + ',' +
              str(h.hospital_score.score_qua) + ',' + str(h.hospital_score.score_oth))
        print(h.name + ' : (1)' + str(round(h_dict['1'], 3)) + '(2)' + str(round(h_dict['2'], 3)) + '(3)' + str(
            round(h_dict['3'], 3)) + '(4)' + str(
            round(h_dict['4'], 3)) + '(5)' + str(round(h_dict['5'], 3)) + '(6)' + str(
            round(h_dict['6'], 3)) + ' count : ' + str(total_artical))

# 將診所分數寫入CSV
def WriteCSV():
    workpath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    c = os.path.join(workpath, '../static/dataset/hospital_score.xlsx')
    hospital = Hospital.objects.all()
    with open(c, 'a', encoding='utf-8-sig', errors='ignore') as csvfile:
        fieldnames = ['Name', 'Economic', 'Temporal', 'Convenience', 'Sociopsychological', 'Quality', 'Other', 'Total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()  # 新增header，第一次才需使用
        for h in hospital:
            writer.writerow(
                {'Name': h.name, 'Economic': h.hospital_score.score_ec, 'Temporal': h.hospital_score.score_tem,
                 'Convenience': h.hospital_score.score_con, 'Sociopsychological': h.hospital_score.score_soc,
                 'Quality': h.hospital_score.score_qua, 'Other': h.hospital_score.score_oth, 'Total': h.hospital_score.total_WOM})




if __name__ == '__main__':
    # ArticalClassification()
    # HospitalScore()
    # WriteCSV()
    print('ya')
