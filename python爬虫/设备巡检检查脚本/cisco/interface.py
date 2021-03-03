import openpyxl
import os
import re
def main():
    filelist = fileBl()
    texttj(filelist)
def fileBl():
    path = "F:/ciscotest"   #指定文件路径
    for root, dirs, files in os.walk(path, True):#进行目录遍历
        print ('root: %s' % root)#输出文件所属目录
        print ('dirs: %s' % dirs)#输出子文件夹
        print ('files:{}'.format(files))#输出文件名
        return(files)
def texttj(files):
    wenjianshu=len(files)
    index=0
    while(wenjianshu):
        with open('F:/ciscotest/'+files[index], encoding="utf-8")as file_object:
            text = file_object.readlines()  # 读取文件内容
            lines = len(text)  # 统计文件行数
            #print(lines)
            name=files[index]
            wenjianshu-=1
            index+=1
            textcz(name,text)
def textcz(filename,textcount):
    for i in range(len(textcount)):
        result=re.search('Processor Pool Total:(.*) Used:(.*) Free:(.*)',textcount[i])
        list1=[]
        list2=[]
        if result!=None:
            #print(result.group(1))
            #print(result.group(2))
            #print(result.group(3))
            list1=[filename,result.group(1),result.group(2),result.group(3)]
            #print(list1)
            num=i+1
            result1=re.search('I/O Pool Total:(.*) Used:(.*) Free:(.*)',textcount[num])
            #print(result1.group(1))
            #print(result1.group(2))
            #print(result1.group(3))
            list2 = [filename,result1.group(1),result1.group(2),result1.group(3)]
            writeexcel(list1,list2)
            break
def writeexcel(li1,li2):
    workbook=openpyxl.load_workbook('F:/memory.xlsx')
    memory1=workbook['memory']
    memory1.append(li1)
    memory1.append(li2)
    workbook.save('F:/memory.xlsx')
if __name__ == '__main__':
    main()