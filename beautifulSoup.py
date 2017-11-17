#-*-coding:utf-8-*-
from bs4 import BeautifulSoup



html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html,'lxml')

# 或者可以用 open('index.html')

# print soup.prettify()
# 用soup 加 标签名 即可获得第一个匹配的元素
print soup.title
print soup.head
print soup.a
print type(soup.a)

print u"------获取属性--------"
print soup.p.get("class")
del soup.p["class"]
print soup.p

print u"------获取标签里的文字----------"
print soup.p.string
for string in soup.strings:
    print(repr(string))
# 给输出的字符串去掉空格或者空行 stripped_strings

print u"------遍历文档树----------"
print soup.head.contents[0]
for child in soup.body.children:
    print child
# 获取所有子孙节点 desendants

print u"------父节点---------"
p = soup.p
print p.parent.name

content = soup.head.title.string
print content.parent.name

# 全部父节点
for parent in content.parents:
    print parent.name

print u"--------兄弟节点------------"
print soup.p.next_sibling
print soup.p.prev_sibling
# 通过 .next_siblings 和 .previous_siblings 属性可以对当前节点的兄弟节点迭代输出

print u"--------前后节点------------"
print soup.head.next_element
print soup.head.previous_element
# 通过 .next_elements 和 .previous_elements 的迭代器就可以向前或向后访问文档的解析内容,就好像文档正在被解析一样

print u"--------搜索文档树-----------"
# find_all(name,attrs,recursive)
soup.find_all(attrs={"data-foo": "value"})
soup.find_all("a", limit=2)
# 调用tag的 find_all() 方法时,Beautiful Soup会检索当前tag的所有子孙节点,如果只想搜索tag的直接子节点,可以使用参数 recursive=False
soup.select("a")
soup.select(".sister") # 根据类名检索
soup.select("#link1") # 根据id 检索


