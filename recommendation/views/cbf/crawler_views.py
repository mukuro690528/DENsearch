import requests
from bs4 import BeautifulSoup
import csv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

# 從各大網站搜集口碑文章、留言

#Facebook

def facebookCrawler():
    driver = webdriver.Chrome('/Users/shan/tools/webdriver/chromedriver')
    driver.set_window_size(1000, 30000)
    driver.get('https://www.facebook.com/pg/揚洋牙醫診所-882975585175869/reviews/?ref=page_internal')
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "_34-w"))
        )
    except TimeoutException:
        print('time out')

    seemore = driver.find_elements_by_class_name('see_more_link')
    for b in seemore:
        driver.execute_script("arguments[0].click();", b)

    contents = driver.find_elements(By.XPATH, './/p')

    workpath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    c = os.path.join(workpath, '../static/dataset/test.csv')
    with open(c, 'a', encoding='utf-8-sig', errors='ignore') as csvfile:
        fieldnames = ['hospital', 'content']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # writer.writeheader()  #新增header，第一次才需使用
        for c in contents:
            writer.writerow({'hospital': '揚洋牙醫診所', 'content': c.text})
            print(c.text)


#PTT

def PTTCrawler():
    url = 'https://www.ptt.cc/bbs/Taoyuan/M.1516275395.A.27D.html' # 選擇要爬的ptt網址，限ptt官方網頁
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html5lib")

    data = {}
    for item in soup.select('.push'):
        name = item.select('span')[1].text
        content = item.select('span')[2].text.strip(': ')
        # print(name + ':' + content)
        if name in data:
            data[name] = data[name] + ' ' + content
        else:
            data[name] = content

    workpath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    c = os.path.join(workpath, 'static/dataset/../../../static/dataset/test.csv')
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



if __name__ == '__main__':
    facebookCrawler()
    # PTTCrawler()