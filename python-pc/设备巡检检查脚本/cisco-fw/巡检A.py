import openpyxl
import os
import re
import memoryA
import versionA
import cpuA
import dirA
import fwresourceA
import listB
import cpuB
import memoryB
import environmentAB
def main():
    filelist = fileBl()
    texttj(filelist)
def fileBl():
    #获取文件数量，返回文件名列表
    path = "D:/xunjian/ciscotest-fw"   #指定文件路径
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
        with open('D:/xunjian/ciscotest-fw/'+files[index], encoding="utf-8")as file_object:
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
            for i in text:
                checkmode=re.search('Security context mode:(.*)',i)
                tl = re.search('WL-FW-C5505# show mode',i)
                if checkmode:
                    if checkmode.group(1)==' multiple ':
                        print('多模防火墙')
                        xqlist=listB.textcz(name,text)
                        versionA.textcz(name, text)
                        dirA.textcz(name, text)
                        fwresourceA.textcz(name, text)
                        environmentAB.textcz(name, text)
                        for i in range(len(xqlist)):
                            count=i
                            cpuB.textcz(name,text, xqlist,count)
                            memoryB.textcz(name,text,xqlist,count)
                    elif checkmode.group(1)==' single ':
                        versionA.textcz(name, text)
                        cpuA.textcz(name, text)
                        memoryA.textcz(name, text)
                        dirA.textcz(name, text)
                        fwresourceA.textcz(name, text)
                        environmentAB.textcz(name, text)
                elif tl:
                    versionA.textcz(name, text)
                    cpuA.textcz(name, text)
                    memoryA.textcz(name, text)
                    dirA.textcz(name, text)
                    fwresourceA.textcz(name, text)
if __name__ == '__main__':
    main()