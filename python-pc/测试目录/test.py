# def zsq(func):
#     print("这个是装饰器外部：")
#     def inner(*num,**kwargs):
#         print("这里是装饰器内部:")
#         func(*num,kwargs)
#     return inner
# @zsq
# def bzs(a,b,c=4,d=15,e=100):
#     print("a是{}，b是{}，c是{}，d是{},e是{}".format(a,b,c,d,e))
# bzs(10,20,c=30,e=50)
# bzs(10,20,30)
# #万能装饰器，定义时用*和**表示元组和字典，调用时也使用对应的*和**来进行解包。如果调用时，没有使用**来解包，那么这个时候
# #因为定义的时候使用**就是创建了一个空字典，就把对应的位置的值给覆盖了，因为空字典也算赋值，后面的不影响
zd={"a":"shdkashjkdas","b":"321y8sabhjdsa"}
def test1(a,b):
    print(a)
    print(b)
test1(**zd)
c,d=(**zd)
print(c,d)