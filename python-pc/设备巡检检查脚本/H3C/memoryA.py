import re
import openpyxl
def textcz(filename,textcount):
    for i in range(len(textcount)-1):
        result=re.search(']display memory',textcount[i])
        if result:
            num = i+1
            result1=re.search('The statistics about memory is measured in KB:',textcount[num])
            result2 = re.search('System Total Memory\(bytes\): (.*)', textcount[num])
            if result1:
                num+=1
                count1=re.search('Slot (.*)',textcount[num])
                while(count1):
                    result3=re.search('Mem:(\s)+?((\d)+)(\s)+?((\d)+)+(\s)+?((\d)+)+(\s)+?',textcount[num + 2])
                    #print(result3.group(0))
                    list1=[filename, result3.group(2), result3.group(5), result3.group(8)]
                    writeexcel(list1)
                    num+=6
                    count1=re.search('Slot (.*)',textcount[num])
                break
            elif result2:
                result4 = re.search('Total Used Memory\(bytes\): (.*)', textcount[num+1])
                result5 = re.search('Used Rate: (.*)', textcount[num+2])
                list1 = [filename, result2.group(1), result4.group(1), result5.group(1)]
                writeexcel(list1)
                break
def writeexcel(li1):
    workbook=openpyxl.load_workbook('D:/xunjian/h3c.xlsx')
    memory1=workbook['memory1']
    memory1.append(li1)
    workbook.save('D:/xunjian/h3c.xlsx')