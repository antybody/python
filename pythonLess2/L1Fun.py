#-*-coding:utf-8-*-
# 动态引用
# __job python 对属性权限的控制是通过属性名来实现的，如果一个属性由双下划线开头（_）该属性就无法被外部访问
# 当实例属性和类属性重名时，实例属性优先级别高
try:
    import json
except ImportError:
    import simplejson as json

print json.dumps({'aa':'bb'})
# 变量也是个函数
print abs(-10)
a = abs
print a(-10)
# 高阶函数
def add(x,y,f):
    return f(x)+f(y)

#
def f1(x):
    return x*2
def new_fn(f):
    def fn(x):
        print 'call' + f._name_ +'()'
        return f(x)
    return fn
# @log 打印日志 监测性能  @performace @post('/register)
print add(-5,9,abs)

# 继承
# 初始化父类 super().__init__()
# isinstance(A,B) 判断A 是不是 B的类型
