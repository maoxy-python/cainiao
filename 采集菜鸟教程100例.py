import urllib.request as requset
from lxml import etree
import MySQLdb


# 发送请求并获取响应
def sendRequest(url):
    res = requset.urlopen(url)
    return res.read().decode('utf-8')  # 拿到的响应：

# 解析响应
def analysisResponse(html):
    # 初始化html
    html = etree.HTML(html)
    # 解析页面
    urls = html.xpath('//div[@id="content"]/ul[1]//li/a/@href')
    return ['http://www.runoob.com' + i for i in urls]

# 通过url解析详情页
def analysisDetails(url):
    html = sendRequest(url)
    # 初始化
    html = etree.HTML(html)
    title = html.xpath('//h1/text()')[0]
    timu = html.xpath('//div[@id="content"]//p[2]/text()')[0]
    res = html.xpath('//div[@id="content"]//p[3]/text()')
    if not res:
        res = ''
    else:
        res = res[0]
    print(title,timu,res)
    return title, timu, res

# 保存数据
def save(param):
    conn = MySQLdb.Connect(host='localhost', user='root', password='123456', db='crawler', port=3306, charset='utf8')
    cursor = conn.cursor()
    sql = 'insert into 100examples(title,topic,parse) VALUES (%s,%s,%s)'
    cursor.execute(sql, param)
    conn.commit()


if __name__ == '__main__':
    html = sendRequest('http://www.runoob.com/python/python-100-examples.html')
    detailsList = analysisResponse(html)
    for i in detailsList:
        analysisDetails(i)
        # save(analysisDetails(i))
