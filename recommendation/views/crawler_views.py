from django.shortcuts import render
import facebook
import requests
from bs4 import BeautifulSoup
import csv
import os

#Facebook

def facebookCrawler():
    token = 'EAACEdEose0cBAKyzveNAmTis2lZAAb62fh0sVCcMbFp9fohjKY4SWuV5KW3UBsqWDYjspsZBSwRaiPtyaThFpjpC0KA99s93KBbkZCaSpBj9cSpLZCgZC5avaEn1MxggbrZBdB8VCqBXbzSMTzYULfWJK0eEh6xLUK8wecUQRVwUl6ZBOo8q7S9jWSw41HiwmALFE9H0Xad7QZDZD'
    graph = facebook.GraphAPI(access_token=token)

    search_list = graph.request('search',{'q': '印象牙醫診所', 'type': 'page'})
    search_id = search_list['data'][0]['id']
    print(search_list)
    print(search_list['data'][0])

    res = requests.get('https://www.facebook.com/pg/'+search_id+'/reviews/?ref=page_internal')
    print(res.text)


    # fanpage_info = graph.get_object('pyladies.tw', field='id')  # 指定拿pyladies.tw 這個粉專的id和讚數
    # print(fanpage_info)  # 印出來看看長什麼樣子，會是JSON格式的資料
    # print("Fanpage id = ", fanpage_info['id'])
    # posts = graph.get_connections(id=fanpage_info['id'], connection_name='posts', summary=True)
    # print(posts)  # 這行會印出一大堆貼文的資料
    # print("共有", len(posts), "篇PO文")



#PTT

def PTTCrawler():
    url = 'https://www.ptt.cc/bbs/Taoyuan/M.1516275395.A.27D.html' #選擇要爬的ptt網址，限ptt官方網頁
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html5lib")
    # print(res.text)

    data = {}
    for item in soup.select('.push'):
        name = item.select('span')[1].text
        content = item.select('span')[2].text.strip(': ')
        # print(name + ':' + content)
        if name in data:
            data[name] = data[name] + ' ' + content
        else:
            data[name] = content
    # print(data)

    workpath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    c = os.path.join(workpath, 'static/dataset/pttWOM_Taoyuan.csv')
    with open(c, 'a', encoding='utf-8-sig', errors='ignore') as csvfile:
        fieldnames = ['name', 'content']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # writer.writeheader()  #新增header，第一次才需使用
        for k in data:
            writer.writerow({'name': k, 'content': data[k]})

    # with open(c, 'r', encoding='utf-8-sig', errors='ignore') as csvfile:
    #     reader = csv.DictReader(csvfile)
    #     for row in reader:
    #         print(row['name']+row['content'])

# facebookCrawler()
PTTCrawler()
