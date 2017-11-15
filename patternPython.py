
# encoding:UTF-8
import re
# 将正则表达式编译成Pattern 对象
pattern = re.comile(r'hello')

result1 = re.match(pattern,'hello')
result2 = re.match(pattern,'hellooooo')

# 如果1匹配成功
if result1:
    print result1.group()
else:
    print "1匹配失败"

# 如果2匹配成功
if result2:
    print result2.group()
else:
    print '2匹配失败'

# 将正则表达式编译成 pattern 对象
pattern1 = re.compile(r'world')
# 使用search() 查找匹配的子串，不存在能匹配的 返回NONE
match = re.search(pattern1,'hello world!')
if match:
    print match.group()
### 输出 ###
# world

# split
pattern2 = re.compile(r'\d+')
print re.split(pattern2,'one1two2three3four4')
## 输出##
#['one','two','three','four','']

#findall
pattern3 = re.compile(r'\d+')
print re.findall(pattern,'one1two2three3four4')
## 输出##
#['1','2','3','4']

#finditer
pattern4 = re.compile(r'\d+')
for m in re.finditer(pattern4,'one1two2three3four4'):
    print m.group()
### 输出 ###
# 1 2 3 4

#sub
pattern5 = re.compile(r'(\w+)(\w+)')
s = 'i say, hello world'

print re.sub(pattern5,r'\2\1',s)

def func(m):
    return m.group(1).title() + ' '+m.group(2).title()

print re.sub(pattern5,func,s)
## output ##
# say i,world hello
# I say,Hello World!