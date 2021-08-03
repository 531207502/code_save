import re
import openpyxl
def textcz(filename,textcount,xqlist,count):
    fp = re.search('(.*)/(.*)', filename)
    if fp:
        filename = fp.group(1)
    if count==0:
        for i in range(len(textcount)):
            result = re.search(filename + '#' + ' show cpu usage', textcount[i])
            if result:
                result1 = re.search('CPU utilization for 5 seconds = (.*); 1 minute: (.*); 5 minutes: (.*)',
                                    textcount[i + 1])
                list1 = [filename , result1.group(1), result1.group(2), result1.group(3)]
                writeexcel(list1)
                break
    else:
        for i in range(len(textcount)):
            result=re.search(filename+'/'+xqlist[count]+'#'+' show cpu usage',textcount[i])
            if result:
                result1 = re.search('CPU utilization for 5 seconds = (.*); 1 minute: (.*); 5 minutes: (.*)',textcount[i+1])
                list1=[filename+'/'+xqlist[count],result1.group(1),result1.group(2),result1.group(3)]
                writeexcel(list1)
                break
def writeexcel(li1):
    workbook=openpyxl.load_workbook('D:/xunjian/cisco-fw.xlsx')
    memory1=workbook['cpu1']
    memory1.append(li1)
    workbook.save('D:/xunjian/cisco-fw.xlsx')
