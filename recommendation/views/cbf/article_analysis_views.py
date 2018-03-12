import os, csv
import jieba
import jieba.posseg as pseg

# 分析口碑文章，建立診所分數
def ArticalClassification():
    workpath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    c = os.path.join(workpath, '../static/dataset/pttWOM_Taoyuan.csv')
    d = os.path.join(workpath, '../static/jiebadict/userdict.txt')

    jieba.load_userdict(d)

    with open(c, "r", encoding='big5', errors='ignore') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            sentence = row['content']
            print("Input：", sentence)
            words = jieba.cut(sentence, cut_all=False)
            # print("Output：" + "/ ".join(words))
            hash = {}
            for word in words:
                if word in hash:
                    hash[word] += 1
                else:
                    hash[word] = 1
            print(hash)




ArticalClassification()