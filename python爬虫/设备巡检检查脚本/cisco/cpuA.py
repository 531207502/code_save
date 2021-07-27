import re
import openpyxl
def textcz(filename,textcount):
    for i in range(len(textcount)):
        result=re.search('CPU utilization for five seconds: (.*); one minute: (.*); five minutes: (.*)',textcount[i])
        result1=re.search('CPU util  :   (.*) user,   (.*) kernel,   (.*) idle',textcount[i])
        result2=re.search('CPU utilization for 5 seconds = (.*); 1 minute: (.*); 5 minutes: (.*)',textcount[i])
        result3=re.search('CPU states  :   (.*) user,   (.*) kernel,   (.*) idle',textcount[i])
        if result:
            list1=[filename,result.group(1),result.group(2),result.group(3)]
            writeexcel(list1)
            break
        elif result1:
            list1 = [filename, result1.group(1)+' user', result1.group(2)+' kernel', result1.group(3)+' idle']
            writeexcel(list1)
            break
        elif result2:
            list1 = [filename, result2.group(1), result2.group(2), result2.group(3)]
            writeexcel(list1)
            break
        elif result3:
            list1 = [filename, result3.group(1) + ' user', result3.group(2) + ' kernel', result3.group(3) + ' idle']
            writeexcel(list1)
            break
def writeexcel(li1):
    workbook=openpyxl.load_workbook('F:/cisco.xlsx')
    memory1=workbook['cpu1']
    memory1.append(li1)
    workbook.save('F:/cisco.xlsx')
