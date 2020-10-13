import re
list_port=["eth 1/101/1/42","eth 1/101/1/26","eth 1/101/1/23","eth 1/101/1/7","eth 1/101/2/46","eth 1/101/1/34","eth 1/101/1/18","eth 1/101/1/13","eth 1/101/1/32","eth 1/101/1/25","eth 1/101/1/45","eth 1/101/2/8"]
print("这个是原来的序列：{}".format(list_port))
list_port1=list_port.copy()
new_list=[]
for i,j in enumerate(list_port1):
    list1=(re.match('eth 1/101/(\d+)/(\d+)',j).groups())
    new_list.append(list1)
# print(sorted(new_list,key=lambda x:x[0]))
new_px=sorted(new_list,key=lambda x:(int(x[0]),int(x[1])))
for i in new_px:
    print("eth 1/101/{}/{}".format(i[0],i[1]),end=",")

