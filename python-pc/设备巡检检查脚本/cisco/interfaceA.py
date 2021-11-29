import re
import openpyxl
from time import sleep
def textcz(filename,textcount):
    for i in range(len(textcount)):
        if(re.search('(.*)show interface$',textcount[i])):
            numstart=i
            print(numstart)
            break
    for j in range(numstart+1,len(textcount)):
        if(re.search('(.*)#(show| show)',textcount[j])):
            break
        else:
            duankou=re.search('^(GigabitEthernet|TenGigabitEthernet|FastEthernet|Serial|Vlan|Loopback|Port-channel)(.*) is up, line protocol is up', textcount[j])
            duankou1=re.search('(Ethernet|port-channel)(.*) is up$',textcount[j])
            list1 =[]
            if(duankou):
                dkname=duankou.group(1)+duankou.group(2)
                num=j
                for k in range (j+1,len(textcount)):
                    if(re.search('(GigabitEthernet|TenGigabitEthernet|FastEthernet|Serial|Vlan|NVI0|Loopback|Port-channel) is',textcount[k])):
                        break
                    else:
                        result1 = re.search('(\d*) input errors, (\d*) CRC, (\d*) frame, (\d*) overrun, (\d*) ignored',textcount[k])
                        result4 = re.search('(\d*) output errors', textcount[k])
                        if(result1):
                            list1.append(filename)
                            list1.append(dkname)
                            list1.append(result1.group(1))
                            list1.append(result1.group(2))
                        elif all((result4,list1)):
                            list1.append(result4.group(1))
                            break
                if(list1):
                    writeexcel(list1)
            elif (duankou1):
                dkname = duankou1.group(1) + duankou1.group(2)
                nun=j
                for k in range(j + 1, len(textcount)):
                    if (re.search(
                            '(Ethernet|port-channel|^mgmt|^Vlan|^loopback)(.*?) is',
                            textcount[k])):
                        break
                    else:
                        result1=re.search('(\d*) runts  (\d*) giants  (\d*) (CRC|CRC/FCS)  (\d*) no buffer',textcount[k])
                        result2=re.search('(\d*) input error  (\d*) short frame  (\d*) overrun   (\d*) underrun  (\d*) ignored',textcount[k])
                        result3=re.search('(\d*) output error  (\d*) collision  (\d*) deferred  (\d*) late collision',textcount[k])
                        if result1:
                            list1.append(filename)
                            list1.append(dkname)
                            list1.append(result1.group(3))
                        elif all((result2,list1)):
                            list1.insert(2,result2.group(1))
                        elif all((result3,list1)):
                            list1.append(result3.group(1))
                if(list1):
                    writeexcel(list1)
def writeexcel(li1):
    workbook=openpyxl.load_workbook('D:/xunjian/cisco.xlsx')
    interface=workbook['interface1']
    interface.append(li1)
    workbook.save('D:/xunjian/cisco.xlsx')