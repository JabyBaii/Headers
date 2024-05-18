#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import datetime

import requests
import feedparser
from flask import Flask, render_template, request, make_response


app = Flask(__name__)

RSS_FEED = {"zhihu": "https://www.zhihu.com/rss",
            "ruanyifeng": "http://www.ruanyifeng.com/blog/atom.xml",
            "songshuhui": "http://songshuhui.net/feed",
            "ifeng": "http://news.ifeng.com/rss/index.xml",
            "news": "http://www.economist.com/rss/the_world_this_week_rss.xml"}

WEATHERS = {"北京": 101010100,
            "上海": 101020100,
            "广州": 101280101,
            "深圳": 101280601}

DEFAULTS = {'city': '上海',
            'publication': 'ifeng'}


def get_value_with_fallback(key):
    if request.args.get(key):
        return request.args.get(key)
    if request.cookies.get(key):
        return request.cookies.get(key)
    return DEFAULTS[key]


# 入口
@app.route('/')
def home():
    # 获取默认值
    publication = get_value_with_fallback('publication')
    city = get_value_with_fallback('city')
    print("检查到页面刷新，获取信息：", publication, city)

    weather = get_weather(city)
    articles = get_news(publication)
    if articles:
        print("content：", articles)
    else:
        print("未获取到 articles 的xml信息，请检查网络或者xml是否可用。")

    # 将articles,weather传递给html
    response = make_response(render_template('home.html', articles=articles, weather=weather))
    # response = make_response(render_template('home.html', articles=articles))

    # # 设置过期时间为1年
    # expires = datetime.datetime.now() + datetime.timedelta(days=365)
    # response.set_cookie('publication',  publication, expires=expires)
    # response.set_cookie('city',  city, expires=expires)

    return response


def get_news(publication):
    feed = feedparser.parse(RSS_FEED[publication])
    return feed['entries']


def get_weather(city):
    # code = WEATHERS.get(city, 101010100)
    code = WEATHERS.get(city)
    # https://e.weather.com.cn/mweather/101280601.shtml
    # url = "https://e.weather.com.cn/mweather/{0}.shtml".format(code)
    url = "http://www.weather.com.cn/data/sk/{0}.html".format(code)
    print("城市代码：", code)
    print("天气链接：", url)

    r = requests.get(url)
    r.encoding = 'utf-8'
    # print(r)

    # 使用BeautifulSoup库来解析html
    from bs4 import BeautifulSoup
    html_content = r.content
    print(html_content)

    soup = BeautifulSoup(html_content, 'html.parser')
    title = soup.find_all('meta')
    print('-----: ', title)

    # data = r.json()['weatherinfo']
    # data = r.text
    # print('data: ', data)
    # return dict(city=data['city'], temperature=data['temp'], description=data['WD'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


# r = requests.get("www.begtut.com")

# from bs4 import BeautifulSoup
# import requests

# url = "https://e.weather.com.cn/mweather/101280601.shtml"
# r = requests.get(url)
# html_content = r.content

# soup = BeautifulSoup(html_content, 'html.parser')

# # 这里你可以使用 BeautifulSoup 的方法来提取你需要的信息
# # 例如，查找标题
# title = soup.title.text
# print(title)

# # 或者查找特定标签
# divs = soup.find_all('div')
# for div in divs:
#     print(div.text.strip())