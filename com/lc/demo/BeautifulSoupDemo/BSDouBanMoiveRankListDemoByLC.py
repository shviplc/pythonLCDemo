# -*- coding: utf-8 -*-
"""
豆瓣电影排行榜
https://movie.douban.com/chart
LC 2018-12-20 14:54:33
爬：豆瓣电影排行榜
"""

from bs4 import BeautifulSoup
import requests, sys


def get_movie_top_list(self):
    req = requests.get(url=self)
    html = req.text
    div_bf = BeautifulSoup(html, "html.parser")

    div = div_bf.find_all('div', class_='indent')
    print(div[0])
    print(div[1]) # top250

    divTop250 = div_bf.find_all('div', class_='douban-top250-bd')
    print(divTop250)

    top_list_bf = BeautifulSoup(str(div[0]), "html.parser")
    a = top_list_bf.find_all('a')
    print(a)

# 得到这样的列表
# [   <a class="nbg" href="https://movie.douban.com/subject/27615441/" title="网络谜踪"><img alt="网络谜踪" class="" src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2542848758.jpg" width="75"/></a>,
#     <a class="" href="https://movie.douban.com/subject/27615441/"> 网络谜踪/ <span style="font-size:13px;">人肉搜寻(港) / 人肉搜索(台)</span></a>,
#
#     <a class="nbg" href="https://movie.douban.com/subject/27102569/" title="悲伤逆流成河"><img alt="悲伤逆流成河" class="" src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2529701498.jpg" width="75"/> </a>,
#     <a class="" href="https://movie.douban.com/subject/27102569/">悲伤逆流成河/ <span style="font-size:13px;">悲伤逆流成河电影版 / Cry Me a Sad River</span></a>
# ]

# 通过class=nbg再次搜索
    a_bf = BeautifulSoup(str(a), "html.parser")
    divToplist_real = a_bf.find_all('a', class_='nbg')
    print(divToplist_real)

    for aMovie in divToplist_real:
        # print(aMovie.get('title'))
        # print(aMovie.get('href'))
        # print((aMovie.contents)[1].get('src'))
        print('电影名称：{0} ，图片链接: {1} ， 豆瓣链接: {2} '.format(aMovie.get('title'),(aMovie.contents)[1].get('src'),aMovie.get('href')))


    print('爬虫完毕！')
    print('永远不要忘记学习!~LC')





if __name__ == "__main__":
    print('开始爬虫了')
    get_movie_top_list("https://movie.douban.com/chart")
