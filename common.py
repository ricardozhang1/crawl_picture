#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib


def get_md5(url):
    m =hashlib.md5()
    url = url.encode('unicode_escape')
    m.update(url)
    return m.hexdigest()



# print(get_md5('https://www.baidu.com/zhihu'))