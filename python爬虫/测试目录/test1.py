def func():
    i=0
    while i <6:
        temp=yield i
        print("temp的值是{}".format(temp))
        i+=1
    return ("已经结束了{}".format(i))
f=func()
f0=next(f)
#f0=f.send(None)
print(f0)
f1=f.send('呵呵呵呵')
print(f1)
f2=f.send('哈哈哈哈')
print(f2)
