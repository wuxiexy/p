import urllib.request       # 用于抓取数据
import time                 # 用于获取时间
import webbrowser           # 用于打开浏览器

# 要添加的js和css，用于处理抓取到的html代码
addJS = "<script type='text/javascript' src='./common.js'></script><link rel='stylesheet' href='./style.css'>"

f = time.strftime('%Y-%m-%d--%H-%M-%S', time.localtime(time.time()))+'.html'    #获取时间
# print(f)          # 获取当前时间

file = urllib.request.urlopen('http://dgfc.dg.gov.cn/dgwebsite_v2/Secondhand/DailyStatement.aspx')  # 打开页面，抓取数据
data = file.read()  # 读取全部

fhandle = open(f, "ab+")        # 将爬取的网页保存在本地
fhandle.write(data)             # 写入文件
fhandle.close()

with open(f, 'a') as i:         # 添加操作的 js文件
   i.write(addJS)

webbrowser.open(f)              # 浏览器打开
