#-*-coding:utf-8-*-


"""
  链接被禁用了
"""
import urllib
import urllib2
import re
import os
import tool

class Spider:
    # 页面初始化
    def __init__(self):
        self.siteURL = 'http://mm.taobao.com/json/request_top_list.htm'
        self.tool = tool.Tool()

    #按页面号获取页面的内容
    def getPage(self,pageIndex):
        url = self.siteURL + "?page=" +str(pageIndex)
        print url
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read().decode('gbk')
    # 获取界面所有MM的信息,list格式
    def getContents(self,pageIndex):
        page = self.getPage(pageIndex)
        pattern = re.compile('<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',re.S)
        items = re.findall(pattern,page)
        contents = []
        for item in items:
            contents.append([item[0],item[1],item[2],item[3],item[4]])
        return contents

    #获取MM个人详情信息
    def getDetailPage(self,infoURL):
        response = urllib2.urlopen(infoURL)
        return response.read().decode('gbk','ignore')

    #获取个人文字简介
    def getBrief(self,page):
        pattern = re.compile('<div class="mm-aixiu-content.*?>(.*?)<!--',re.S)
        result = re.search(pattern,page)
        return self.tool.replace(result.group(1))

    #获取页面所有图片
    def getAllImg(self,page):
        pattern = re.compile('<div class="mm-aixiu-content.*?>(.*?)<!--',re.S)
        content = re.search(pattern,page)
        #从代码中提取图片
        patterImg = re.compile('<img.*?src="(.*?)"',re.S)
        images = re.findall(patterImg,content.group(1))
        return images

    #保存多张写真图片
    def saveImgs(self,images,name):
        number =1
        print u"发现",name,u"共有",len(images),u"张照片"
        for imageURL in images:
            splitPath = imageURL.split('.')
            fTail = splitPath.pop()
            if len(fTail) > 3:
                fTail = "jpg"
            fileName = name +"/"+str(number)+"."+fTail
            self.saveImg(imageURL,fileName)
            number +=1

    #保存头像
    def saveIcon(self,iconURL,name):
        splitPath = iconURL.split(".")
        fTrail = splitPath.pop()
        fileName = name +"/icon."+fTrail
        self.saveImg("http:"+iconURL,fileName)

    # 保存个人简介
    def saveBrief(self,content,name):
        fileName = name + "/" +name +".txt"
        f = open(fileName,"w+")
        print u"正在偷偷保存他的信息",fileName
        f.write(content.encode("utf-8"))

    #传入图片地址，文件名，保存单张图片
    def saveImg(self,imageURL,fileName):
        u = urllib.urlopen(imageURL)
        data = u.read()
        f = open(fileName,'wb')
        print u"正在保存他的图片",fileName
        f.close()

    # 写入文件
    def saveBrif(self,content,name):
        fileName = name +"/"+name+".txt"
        f = open(fileName,"w+")
        print u"正在保存他的个人信息",fileName
        f.write(content.encode('utf-8'))

    #创建新目录
    def mkdir(self,path):
        path = path.strip()
        # 判断路径是否存在
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path)
            return True
        else:
            return False

    #将一页淘宝MM 的信息保存起来
    def savePageInfo(self,pageIndex):
        #获取第一页淘宝MM列表
        contents = self.getContents(pageIndex)
        for item in contents:
            detailURL = item[0]
            detailPage = self.getDetailPage("http:"+detailURL)
            brief = self.getBrief(detailPage)
            images = self.getAllImg(detailPage)
            self.mkdir(item[2])
            self.saveBrief(brief,item[2])
            self.saveIcon(item[1],item[2])
            self.saveImgs(images,item[2])
    #传入起止页码，获取MM图片
    def savePagesInfo(self,start,end):
        for i in range(start,end+1):
            print u"正在找寻"
            self.savePageInfo(i)

spider = Spider()
spider.savePagesInfo(2,10)