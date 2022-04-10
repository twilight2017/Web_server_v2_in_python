import urllib.request as req
baseurl = 'http://c.biancheng.net/view/'
basef = 'e://clan'
for i in range(2999):
    try:
        url = baseurl+str(i+1)+'.html'
        print('url', url)
        webpage = req.urlopen(url) # 根据超链访问链接的网页
        print('webpage', webpage)
        data = webpage.read() # 读取超链网页数据
        print('data', data)
        data = data.decode('utf-8') # byte类型解码为字符串
        f = basef + '/' + str(i+1)+'.html'
        print("f", f)
        txtf = open(f, 'w', encoding='utf-8')
        txtf.write(data)
        txtf.close()
    except:
        print('失败爬取html:'+str(i+1)+'\n')