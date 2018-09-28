# 获取页面
import urllib.request

# 时间
from datetime import date
import time
import sys
import re

# 解析html
from html.parser import HTMLParser


import webbrowser


addJS = "<script type='text/javascript' src='./common.js'></script>"


# now = date.today().strftime('%Y-%m-%d')
# print(now)

# print sys.argv[0]#获得的是当前执行脚本的位置（若在命令行执行的该命令，则为空）
p = sys.argv[0]
print(p)


# now =  + time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
# print(now)          # 获取当前时间
now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+".html"
print(now)                   # 获取当前时间
print(date.today())          # 获取当前时间


file = urllib.request.urlopen('http://dgfc.dg.gov.cn/dgwebsite_v2/Secondhand/DailyStatement.aspx')
data = file.read()  # 读取全部


# dataLine = file.readline()  # 读取一行内容
# print(data)


f = date.today().strftime('%Y-%m-%d')+'.html'


fhandle = open(f, "ab+")    # 将爬取的网页保存在本地
fhandle.truncate()          # 先清空文件
fhandle.write(data)         # 写入文件
fhandle.close()


# 添加操作的 js文件
with open(f, 'a') as i:
   i.write(addJS)


webbrowser.open(f)      # 浏览器打开


