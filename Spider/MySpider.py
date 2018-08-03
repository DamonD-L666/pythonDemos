#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/7/11 10:49
# @Author : Damon
# @Site : 
# @File : MySpider.py
# @Software: PyCharm
# @Description:
# 打开网页，获取网页内容
import urllib.request
import pymysql
import re
import time

# 获取需要的信息
def getFormatMsg(data):
    img_pat = '"pic_url":"(//.*?)"'
    name_pat = '"raw_title":"(.*?)"'
    nick_pat = '"nick":"(.*?)"'
    price_pat = '"view_price":"(.*?)"'
    fee_pat = '"view_fee":"(.*?)"'
    sales_pat = '"view_sales":"(.*?)"'
    comment_pat = '"comment_count":"(.*?)"'
    city_pat = '"item_loc":"(.*?)"'
    detail_url_pat = 'detail_url":"(.*?)"'
    # 查找满足匹配规则的内容，并存在列表中
    imgL = re.compile(img_pat).findall(data)
    nameL = re.compile(name_pat).findall(data)
    nickL = re.compile(nick_pat).findall(data)
    priceL = re.compile(price_pat).findall(data)
    feeL = re.compile(fee_pat).findall(data)
    salesL = re.compile(sales_pat).findall(data)
    commentL = re.compile(comment_pat).findall(data)
    cityL = re.compile(city_pat).findall(data)
    detail_urlL = re.compile(detail_url_pat).findall(data)
    print('长度:',len(nameL))
    print('数据:',nameL)


def url_open(url):
    headers = ("user-agent",
               "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
    return data


keywd = '短裙'
keywords = urllib.request.quote(keywd)
netBeginTime = time.time()
#data = url_open("https://s.taobao.com/search?q=" + keywords)
data = url_open("https://search.jd.com/Search?keyword="+keywords+"&enc=utf-8&wq="+keywords+"&pvid=88082f163ace4aa694f206bfc7138c95")
print('netTime cause: ', str(time.time() - netBeginTime))
#print(data)

handleTime = time.time()
#res_script = "<script>(.*?)</script>"  # 粗粒度筛选
res_script = "<ul>(.*?)</ul>"  # 粗粒度筛选
m_tr = re.findall(res_script, data, re.S | re.M)
print(m_tr)

# for i in range(len(m_tr)):
#     print(str(i)+':'+m_tr[i])
#     if i==3:
#         print('类型:',type(m_tr[i]))
#print(type(m_tr))
#getFormatMsg(m_tr[3])
#print('handleTime cause: ', str(time.time() - handleTime))