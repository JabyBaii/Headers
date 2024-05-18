#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import datetime

import requests
import feedparser
from flask import Flask, render_template, request, make_response


app = Flask(__name__)

RSS_FEED = {"zhihu": "https://www.zhihu.com/rss",
            "netease": "http://news.163.com/special/00011K6L/rss_newsattitude.xml",
            "songshuhui": "http://songshuhui.net/feed",
            "ifeng": "http://news.ifeng.com/rss/index.xml"}

DEFAULTS = {'city': '上海',
            'publication': 'songshuhui'}

WEATHERS = {"北京": 101010100,
            "上海": 101020100,
            "广州": 101280101,
            "深圳": 101280601}


def get_value_with_fallback(key):
    if request.args.get(key):
        return request.args.get(key)
    if request.cookies.get(key):
        return request.cookies.get(key)
    return DEFAULTS[key]

@app.route('/book/被讨厌的勇气')
def book_1():
    response = make_response(render_template('被讨厌的勇气：“自我启发之父”阿德勒的哲学课 (5_15_2024 12_38_10 AM).html'))
    return response

@app.route('/book/居里夫人自传')
def book_2():
    response = make_response(render_template('居里夫人自传 (5_16_2024 1_48_54 AM).html'))
    return response

@app.route('/book/斯大林传')
def book_3():
    response = make_response(render_template('斯大林传 (5_16_2024 1_31_05 AM).html'))
    return response

@app.route('/book/马斯克传')
def book_4():
    response = make_response(render_template('埃隆·马斯克传 (5_16_2024 2_08_48 AM).html'))
    return response

@app.route('/book/乔布斯传')
def book_5():
    response = make_response(render_template('史蒂夫•乔布斯传(Steve Jobs_A Biography) (5_16_2024 2_12_17 AM).html'))
    return response

@app.route('/book/毛泽东传')
def book_6():
    response = make_response(render_template('毛泽东传_名著珍藏版(插图本)（完整版） (5_16_2024 2_19_27 AM).html'))
    return response

@app.route('/book/人生海海')
def book_516_1():
    response = make_response(render_template('人生海海 (5_16_2024 6_43_04 PM).html'))
    return response

@app.route('/book/你当像鸟飞往你的山')
def book_516_2():
    response = make_response(render_template('你当像鸟飞往你的山 (5_16_2024 6_29_26 PM).html'))
    return response

@app.route('/book/少有人走的路')
def book_516_3():
    response = make_response(render_template('少有人走的路(1-8全套) (5_16_2024 9_45_59 PM).html'))
    return response

@app.route('/book/心流')
def book_516_4():
    response = make_response(render_template('心流_发现心流（套装全2册） (5_16_2024 6_32_19 PM).html'))
    return response

@app.route('/book/人间值得')
def book_516_5():
    response = make_response(render_template('人间值得 (5_16_2024 4_42_03 PM).html'))
    return response

@app.route('/book/牧羊少年奇幻之旅')
def book_516_6():
    response = make_response(render_template('牧羊少年奇幻之旅 (5_16_2024 5_58_51 PM).html'))
    return response

@app.route('/book/罪与罚')
def book_516_7():
    response = make_response(render_template('罪与罚 (名著名译丛书) (5_16_2024 6_36_21 PM).html'))
    return response

@app.route('/book/被淹没与被拯救的')
def book_516_8():
    response = make_response(render_template('被淹没与被拯救的 (5_16_2024 6_47_20 PM).html'))
    return response

@app.route('/book/费曼学习法')
def book_516_9():
    response = make_response(render_template('费曼学习法（用输出倒逼输入） (5_16_2024 5_46_16 PM).html'))
    return response

@app.route('/book/自控力2')
def book_516_0():
    response = make_response(render_template('xx.html'))
    return response

@app.route('/book/算法图解')
def book_518_0():
    response = make_response(render_template('算法图解 (5_18_2024 5_38_10 PM).html'))
    return response

@app.route('/book/程序员的自我修养')
def book_518_1():
    response = make_response(render_template('程序员的自我修养 (5_18_2024 5_52_00 PM).html'))
    return response

@app.route('/book/挪威的森林')
def book_518_2():
    response = make_response(render_template('挪威的森林 (5_18_2024 4_31_09 PM).html'))
    return response

@app.route('/book/我有一只叫抑郁症的黑狗')
def book_518_3():
    response = make_response(render_template('我有一只叫抑郁症的黑狗 (5_18_2024 5_03_37 PM).html'))
    return response

@app.route('/book/底层逻辑 看清这个世界的底牌')
def book_518_4():
    response = make_response(render_template('底层逻辑 看清这个世界的底牌 (5_18_2024 5_51_20 PM).html'))
    return response

@app.route('/book/底层逻辑2：理解商业世界的本质')
def book_518_5():
    response = make_response(render_template('底层逻辑2：理解商业世界的本质 (5_18_2024 5_47_02 PM).html'))
    return response

@app.route('/book/如何成为不完美主义者')
def book_518_6():
    response = make_response(render_template('如何成为不完美主义者 (5_18_2024 4_18_14 PM).html'))
    return response

@app.route('/book/人性的弱点')
def book_518_7():
    response = make_response(render_template('人性的弱点 (5_18_2024 4_12_45 PM).html'))
    return response

@app.route('/')
def home():
    publication = get_value_with_fallback('publication')
    city = get_value_with_fallback('city')

    # weather = get_weather(city)
    # articles = get_news(publication)
    weather = []
    articles = []
    

    response = make_response(render_template('book.html', articles=articles, weather=weather))

    # expires = datetime.datetime.now() + datetime.timedelta(days=365)
    # response.set_cookie('publication',  publication, expires=expires)
    # response.set_cookie('city',  city, expires=expires)

    return response


def get_news(publication):
    feed = feedparser.parse(RSS_FEED[publication])
    return feed['entries']


def get_weather(city):
    code = WEATHERS.get(city, 101010100)
    url = "http://www.weather.com.cn/data/sk/{0}.html".format(code)

    r = requests.get(url)
    r.encoding = 'utf-8'

    data = r.json()['weatherinfo']
    print(data)
    return dict(city=data['city'], temperature=data['temp'],
                description=data['WD'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)