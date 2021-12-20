import openpyxl
import os
import re
import interfaceA
import memoryA
import versionA
import cpuA
import dirA
import environment
import spanningtree
def main():
    filelist = fileBl()
    texttj(filelist)
def fileBl():
    #获取文件数量，返回文件名列表
    path = "D:/xunjian/ciscotest"   #指定文件路径
    for root, dirs, files in os.walk(path, True):#进行目录遍历
        print ('root: %s' % root)#输出文件所属目录
        print ('dirs: %s' % dirs)#输出子文件夹
        print ('files:{}'.format(files))#输出文件名
        return(files)
def texttj(files):
    #统计文件数，打开文件统计每个文件行数，传递文件名及文本列表
    wenjianshu=len(files)
    index=0
    while(wenjianshu):
        with open('D:/xunjian/ciscotest/'+files[index], encoding="utf-8")as file_object:
            text = file_object.readlines()  # 读取文件内容
            lines = len(text)  # 统计文件行数
            #print(lines)
            for i in text:
                name1=re.search('(.*)show version',i)
                if(name1):
                    name1=name1.group(1)
                    #print(name1)
                    break
            name=name1
            wenjianshu-=1
            index+=1
            versionA.textcz(name,text)
            cpuA.textcz(name,text)
            memoryA.textcz(name,text)
            dirA.textcz(name,text)
            environment.textcz(name,text)
            spanningtree.textcz(name,text)
            #interfaceA.textcz(name,text)
if __name__ == '__main__':
    main()
    #核心的好像总数是46台，加北京4台
