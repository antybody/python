# -*- coding: utf-8 -*-
"""
Description:python2.7
    A simple web spider for bd
Author:     435612413@qq.com
Created Date:   2017-11-15
Version:        2017-11-15
"""
import urllib2
import urllib
import re

#处理页面标签类
class Tool:
    #去除img标签，7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    #删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    #把换行的标签换成\n
    replaceline = re.compile('<tr>|<div>|</div>|</p>')
    # 将表格制表<td>替换为\t
    replaceTD = re.compile('<td>')
    #把段落开头换位\n 加空两个空格
    replacePara = re.compile('<p.*?>')
    #将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    #将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceline,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replacePara,"\n",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        return x.strip()
#百度贴吧爬虫类
class BDTB:
    # 初始化，传入基地址，是否只看楼主的参数
    def __init__(self,baseUrl,seelZ,floorTag):
        self.baseURL = baseUrl
        self.seelZ = '?see_lz='+str(seelZ)
        self.tool = Tool()
        self.file = None
        self.floor = 1
        self.defaultTitle = u'百度贴吧'
        self.floorTag = floorTag

    #传入页码，获取该页帖子的代码
    def getPage(self,pageNum):
        try:
            url = self.baseURL+ self.seelZ+'&pn='+str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            # print response.read()
            return response.read().decode('utf-8','ignore') #忽略编码不成功的数据
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print u"连接百度贴吧失败，错误原因",e.reason
                return None
    # 获取帖子的标题
    def getTile(self,page):
        # page = self.getPage(1)
        pattern = re.compile('<h1 class="core_title_txt.*?>(.*?)</h1>', re.S)
        result = re.search(pattern,page)
        if result:
            return result.group(1).strip()
        else:
            return None

    #提取帖子页数
    def getPageNum(self,page):
        # page = self.getPage(1)
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span class="red.*?>(.*?)</span>',re.S)
        result = re.search(pattern,page)
        if result:
            return result.group(1).strip()
        else:
            return None

    #获取正文内容
    def getContent(self,page):
        # page = self.getPage(1)
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
        items = re.findall(pattern,page)
        contents = []
        for item in items:
            # print flour,u'楼--------------------------------------------'
            # print self.tool.replace(item)
            # flour +=1
            content = "\n" +self.tool.replace(item)+"\n"
            contents.append(content.encode('utf-8'))
        return contents

    # 如果标题不是none ,表示成功获取到标题
    def setFileTile(self,title):
        if title is not None:
            self.file = open(title +".txt",'w+')
        else:
            self.file = open(self.defaultTitle +".txt","w+")

    # 向文件中写入数据
    def writeData(self,contents):
        for item in contents:
            if self.floorTag == "1":
                floorLine = "\n" +str(self.floor)+u"----------------------------\n"
                self.file.write(floorLine)
                self.file.write(item)
                self.floor +=1

    # 启动文件
    def start(self):
        indexPage = self.getPage(1)
        pageNum = self.getPageNum(indexPage)
        title = self.getTile(indexPage)
        self.setFileTile(title)
        if pageNum == None:
            print u"URL 失效，请重试"
            return
        try:
            print u"该梯子共有"+str(pageNum)+u"页"
            for i in range(1,int(pageNum)+1):
                print u"正在写入第"+str(i)+u"页数据"
                page = self.getPage(i)
                contents = self.getContent(page)
                self.writeData(contents)
        except IOError,e:
            print u"写入异常，原因" + e.message
        finally:
            print u"写入任务完成"

print u"请输入帖子代号"
baseURL = "http://tieba.baidu.com/p/"+str(raw_input(u'http://tieba.baidu.com/p/'))
seeLZ = raw_input(unicode("是否只获取楼主发言，是输入1，否输入0\n",'utf-8').encode('gbk'))
floorTag = raw_input(unicode("是否写入楼层信息，是输入1，否输入0\n",'utf-8').encode('gbk'))
bdtb = BDTB(baseURL,seeLZ,floorTag)
bdtb.start()