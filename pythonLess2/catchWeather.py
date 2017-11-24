#-*-coding:utf-8-*-
'''
 Coding by yuanmin,20171121
 抓取网站上各监测站点实时数据
 插入MySQL 数据库，并且生成json 文件
'''
import urllib2
import urllib
import re
import tool
import myConnect
import json
from bs4 import BeautifulSoup, NavigableString


# 抓取网站上PM信息
class PMXX:
    # 获取地址
    def __init__(self,baseURL):
        self.baseURL = baseURL
        self.file = None
        self.tool = tool.Tool()

    # 获取网站上整个页面内容
    def get_html(self):
        try:
            url = self.baseURL
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
             # print response.read()
            return response.read().decode('utf-8', 'ignore')  # 忽略编码不成功的数据
        except urllib2.URLError, e:
             if hasattr(e, "reason"):
                 print u"获取网站内容失败，失败原因", e.reason
                 return None

    # 获取页面table信息
    def get_data(self,page):
        try:
            soup = BeautifulSoup(page, 'lxml')
            contents = []

            for tr in soup.find_all("tr"):
                content = []
                index =0
                for td in tr.find_all("td"):
                    # print td.string
                    index +=1
                    if td.string != None:
                        nums =  re.findall(r"\d+\.?\d*", td.string)
                        # if isinstance(td.string,NavigableString) :
                        #     content.append(td.string)
                        #     print "ok"
                        # else:
                        #     content.append(td.string)
                        if nums.__len__():
                            content.append(nums[0])
                        else:
                            if index == 5 or index ==6 :
                                content.append("0")
                            else:
                                content.append(unicode(td.string))
                contents.append(content)
            return contents
        except:
            print u"转换失败"

    # 输出数据到 MySQL
    def out_mysql(self,config,datalist):
        try:
            db = myConnect.myconnect(config)
            dbConn = db.get_conn()
            dbCursor = dbConn.cursor()
            sql_text = "insert into tb_weather(district,station,AQI,pm25,pm10) VALUES (%s,%s,%s,%s,%s)"
            for dlist in datalist:
                if dlist.__len__():
                    db.get_insert(dbCursor, sqltext=sql_text, sqlparam=dlist)
                    dbConn.commit()
        except:
            print u"输出数据失败"

    # 输出到json 文件
    # key:输出json主键
    # datalist:获取的数据
    def out_json(self,file,key,datalist):
        #对datalist 进行json 处理
        jsonArr =[]
        for dt in datalist:
            js ={}
            flag = 0
            for d in dt:
                js[key[flag]] = dt[flag]
                flag += 1
            jsonArr.append(js)
        # 写入文件
        fileName = "D:\projects\mobile\Python\python\pythonLess2"+"\station.json"
        f = open(fileName, "w+")
        print u"正在保存站点信息", fileName
        json.dump(jsonArr, f, indent=4)

#
baseURL = "http://www.86pm25.com/city/shanghai.html"
if __name__ == "__main__":
    pm = PMXX(baseURL)
    pm_html = pm.get_html()
    pm_data = pm.get_data(pm_html)
    for a in pm_data:
        print a
    config = {
        'host': '101.37.252.24',
        'user': 'root',
        'password': 'root123456',
        'port': 8085,
        'database': 'imap',
        'charset': 'utf8'
    }
    # 调用写入SQL
    in_data = pm.out_mysql(config,pm_data)
    # 调用写入JSON
    fileName = "D:"
    key =["district","station","AQI","pm25","pm10"]
    pm.out_json(fileName,key,pm_data)
