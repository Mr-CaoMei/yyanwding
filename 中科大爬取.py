import requests
from bs4 import BeautifulSoup


def pyspider(target, url, total):
    index = 1
    '''headers = {
        'Cookie': 'Hm_lvt_b3b075d90cc24dcb1d5795260f02e2d6 = 1637129339;Hm_lpvt_b3b075d90cc24dcb1d5795260f02e2d6 = 1637131178',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }'''
    summer = {}
    change = {}
    for i in range(total):
        index += i
        target1 = target + str(index)
        req = requests.get(url=target1)
        req.encoding = 'utf-8'
        html = req.text
        bs = BeautifulSoup(html, 'lxml')
        texts = bs.find('div', class_='r-box')
        texts = texts.find_all('a')
        for text in texts:
            url1 = url + text.get('href')
            title = text.string
            if "2021" in title:
                if "夏令营" in title:
                    summer[str(title)] = str(url1)
            elif "2021" in title:
                if "调剂" in title:
                    change[str(title)] = str(url1)
    return summer, change


if __name__ == "__main__":
    # index = 1
    '''headers = {
        'Cookie': 'Hm_lvt_b3b075d90cc24dcb1d5795260f02e2d6 = 1637129339;Hm_lpvt_b3b075d90cc24dcb1d5795260f02e2d6 = 1637131178',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }'''
    # 中科大链接夏令营与调剂
    target = "https://gradschool.ustc.edu.cn/column/9?current="
    url = "https://gradschool.ustc.edu.cn/"
    totalPage = 8
    summer, change = pyspider(target, url, totalPage)  # summer夏令营  change调剂
    print(summer)
    print(change)