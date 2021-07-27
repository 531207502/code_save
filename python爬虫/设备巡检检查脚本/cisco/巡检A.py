import openpyxl
import os
import re
import interfaceA
import memoryA
import versionA
import cpuA
import dirA
import environment
def main():
    filelist = fileBl()
    texttj(filelist)
def fileBl():
    #获取文件数量，返回文件名列表
    path = "F:/ciscotest"   #指定文件路径
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
        with open('F:/ciscotest/'+files[index], encoding="utf-8")as file_object:
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
            #interfaceA.textcz(name,text)
# def textcz(filename,textcount):
#     for i in range(len(textcount)):
#         if(re.search('(.*)show interface$',textcount[i])):
#             numstart=i
#             print(numstart)
#             break
#     for j in range(numstart+1,len(textcount)):
#         if(re.search('(.*)#show',textcount[j])):
#             break
#         else:
#             duankou=re.search('GigabitEthernet(.*) is up, line protocol is up', textcount[j])
#             if(duankou):
#                 dkname=duankou.group(1)
#                 num=j
#                 list1=[]
#                 for k in range (j+1,len(textcount)):
#                     if(re.search('^GigabitEthernet',textcount[k])):
#                         break
#                     else:
#                         result1 = re.search('(\d*) input errors, (\d*) CRC, (\d*) frame, (\d*) overrun, (\d*) ignored',textcount[k])
#                         result2 = re.search('(\d*) watchdog, (\d*) multicast, (\d*) pause input',textcount[k])
#                         result3 = re.search('(\d*) input packets with dribble condition detected',textcount[k])
#                         result4 = re.search('(\d*) output errors, (\d*) collisions, (\d*) interface resets', textcount[k])
#                         result5 = re.search('(\d*) babbles, (\d*) late collision, (\d*) deferred', textcount[k])
#                         result6 = re.search('(\d*) lost carrier, (\d*) no carrier, (\d*) PAUSE output', textcount[k])
#                         result7 = re.search('(\d*) output buffer failures, (\d*) output buffers swapped out', textcount[k])
#                         if(result1):
#                             list1.append(filename)
#                             list1.append(dkname)
#                             list1.append(result1.group(1))
#                             list1.append(result1.group(2))
#                             list1.append(result1.group(3))
#                             list1.append(result1.group(4))
#                             list1.append(result1.group(5))
#                         elif(result2):
#                             list1.append(result2.group(1))
#                             list1.append(result2.group(2))
#                             list1.append(result2.group(3))
#                         elif(result3):
#                             list1.append(result3.group(1))
#                         elif(result4):
#                             list1.append(result4.group(1))
#                             list1.append(result4.group(2))
#                             list1.append(result4.group(3))
#                         elif(result5):
#                             list1.append(result5.group(1))
#                             list1.append(result5.group(2))
#                             list1.append(result5.group(3))
#                         elif(result6):
#                             list1.append(result6.group(1))
#                             list1.append(result6.group(2))
#                             list1.append(result6.group(3))
#                         elif(result7):
#                             list1.append(result7.group(1))
#                             list1.append(result7.group(2))
#                 #print(list1)
#                 writeexcel(list1)
# def writeexcel(li1):
#     workbook=openpyxl.load_workbook('F:/cisco.xlsx')
#     interface=workbook['interface']
#     interface.append(li1)
#     workbook.save('F:/cisco.xlsx')
if __name__ == '__main__':
    main()