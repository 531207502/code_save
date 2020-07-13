import csv
def write2_csv():
    headers = ["name","age","height"]
    values = [("张三","20","160"),
              ("李四","30","170"),
              ("王五","40","180")
              ]
    with open('cs2.csv','w',encoding="utf-8",newline="") as fp:
#其实这里fp已经可以操作了，这里csv.writer还是下面的csv.reader实际上都是为了把他保存或者读取的时候用csv的格式，然后后面也可以按照csv的标准进行操作
        writer = csv.writer(fp)
        #print(type(writer))
        writer.writerow(headers)
        writer.writerows(values)
#通过字典的方式进行值的写入
def write_csv():
    headers = ["name","age","height"]
#使用列表将多个字典包裹起来
    values = [{"name":"张三","age":"10","height":"160"},
              {"name":"李四","age":"20","height":"170"},
              {"name":"王五","age":"30","height":"180"}
              ]
#采用utf-8的方式进行编码，同时取消每行的空格
    with open('cs.csv','w',encoding="utf-8",newline="") as fp:
#创建字典头，记住创建以后需要调用才行，这里我理解的就相当于定义了字典的key，后面的数据就按照这样的key来进行一一对应
        writer = csv.DictWriter(fp,headers)
        writer.writeheader()
        #这种是取多行数据
        writer.writerows(values)
        #这种就是只取一行数据
        writer.writerow(values[0])
def read2_csv():
    with open('cs.csv','r',encoding='utf-8') as fp:
        reader = csv.reader(fp)
        #print(type(reader))
        next(reader)
        for i in reader:
            #print(i)
            print("name:{},age:{},height:{}".format(i[0],i[1],i[2]))
def read_csv():
    with open('cs2.csv', 'r', encoding='utf-8') as fp:
        reader = csv.DictReader(fp)
        for i in reader:
            #print(i)
            print("name:{},age:{},height:{}".format(i["name"],i["age"],i["height"]))
if __name__=='__main__':
    write_csv()
    write2_csv()
    read2_csv()
    read_csv()
