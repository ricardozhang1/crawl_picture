#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
import os
from utils.common import get_md5


heders = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

def get_page_id(url):
    response = requests.get(url)
    all_pic = re.findall('data-wallpaper-id="(\d+)"',response.text)
    return all_pic


def download_picture(pic_url):
    try:
        if not os.path.exists('img_picture'):
            os.mkdir('img_picture')
        picture = requests.get(pic_url,headers=heders,stream=True)
        filename = ('E:/pythonwork/spiderworks/scraping/articlespider/articlespider/picture_spider/img_picture/' + get_md5(pic_url) + '.jpg')
        pass
        with open(filename,'wb') as f:
            f.write(picture.content)
            f.close()
    except:
        print('下载图片出错！',get_md5(pic_url))


def get_next_page():
    url_list = []
    for i in range(999):
        url_de = 'https://alpha.wallhaven.cc/search?page={0}'.format(i+1)
        url_list.append(url_de)
    return url_list


def download_pic(detail_list):
    for a_url in detail_list:

        download_url = 'https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-{0}.jpg'.format(a_url)
        print(download_url)#打印出下载图片的
        download_picture(download_url)
    return


if __name__ == '__main__':

    url = get_next_page()
    print(url)
    for i in url:
        print(i)#打印出爬取页的url
        detail_list = get_page_id(i)
        download_pic(detail_list)




