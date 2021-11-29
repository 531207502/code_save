import re
import openpyxl
def textcz(filename,textcount,xqlist,count):
    fp = re.search('(.*)/(.*)', filename)
    if fp:
        fp1 = re.search('(.*)/(.*)/(.*)#', filename)
        if fp1:
            filename = fp1.group(1)+fp1.group(2)+fp1.group(3)
        else:
            filename = fp.group(1)
    if count==0:
        for i in range(len(textcount)):
            result = re.search(filename + '#' + ' show memory', textcount[i])
            if result:
                result1 = re.search('Used memory:   (.*)',textcount[i + 2])
                result2 = re.search('Total memory:   (.*)',textcount[i + 4])
                list1 = [filename , result1.group(1), result2.group(1)]
                writeexcel(list1)
                break
    else:
        for i in range(len(textcount)):
            result=re.search(filename+'/'+xqlist[count]+'#'+' show memory',textcount[i])
            if result:
                result1 = re.search('Used memory:   (.*)',textcount[i+1])
                result2 = re.search('Total memory:   (.*)',textcount[i + 3])
                list1 = [filename +'/'+xqlist[count], result1.group(1), result2.group(1)]
                writeexcel(list1)
                break
def writeexcel(li1):
    workbook=openpyxl.load_workbook('D:/xunjian/cisco-fw.xlsx')
    memory1=workbook['memory1']
    memory1.append(li1)
    workbook.save('D:/xunjian/cisco-fw.xlsx')
