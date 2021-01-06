list1=["abc",'23',"程",'9',"tyest",'81',"没有了"]
num=len(list1)
result=[int(x)*int(x) for x in list1 if x.isdigit()]
result1=[int(x)+10 if int(x)<10 else int(x)-10 for x in list1 if x.isdigit()]
print(result)
print(result1)