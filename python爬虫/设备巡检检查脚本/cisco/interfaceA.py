import re
def textcz(filename,textcount):
    for i in range(len(textcount)):
        if(re.search('(.*)show interface$',textcount[i])):
            numstart=i
            print(numstart)
            break
    for j in range(numstart+1,len(textcount)):
        if(re.search('(.*)#show',textcount[j])):
            break
        else:
            duankou=re.search('GigabitEthernet(.*) is up, line protocol is up', textcount[j])
            if(duankou):
                dkname=duankou.group(1)
                num=j
                list1=[]
                for k in range (j+1,len(textcount)):
                    if(re.search('^GigabitEthernet',textcount[k])):
                        break
                    else:
                        result1 = re.search('(\d*) input errors, (\d*) CRC, (\d*) frame, (\d*) overrun, (\d*) ignored',textcount[k])
                        result2 = re.search('(\d*) watchdog, (\d*) multicast, (\d*) pause input',textcount[k])
                        result3 = re.search('(\d*) input packets with dribble condition detected',textcount[k])
                        result4 = re.search('(\d*) output errors, (\d*) collisions, (\d*) interface resets', textcount[k])
                        result5 = re.search('(\d*) babbles, (\d*) late collision, (\d*) deferred', textcount[k])
                        result6 = re.search('(\d*) lost carrier, (\d*) no carrier, (\d*) PAUSE output', textcount[k])
                        result7 = re.search('(\d*) output buffer failures, (\d*) output buffers swapped out', textcount[k])
                        if(result1):
                            list1.append(filename)
                            list1.append(dkname)
                            list1.append(result1.group(1))
                            list1.append(result1.group(2))
                            list1.append(result1.group(3))
                            list1.append(result1.group(4))
                            list1.append(result1.group(5))
                        elif(result2):
                            list1.append(result2.group(1))
                            list1.append(result2.group(2))
                            list1.append(result2.group(3))
                        elif(result3):
                            list1.append(result3.group(1))
                        elif(result4):
                            list1.append(result4.group(1))
                            list1.append(result4.group(2))
                            list1.append(result4.group(3))
                        elif(result5):
                            list1.append(result5.group(1))
                            list1.append(result5.group(2))
                            list1.append(result5.group(3))
                        elif(result6):
                            list1.append(result6.group(1))
                            list1.append(result6.group(2))
                            list1.append(result6.group(3))
                        elif(result7):
                            list1.append(result7.group(1))
                            list1.append(result7.group(2))
                #print(list1)
                writeexcel(list1)
def writeexcel(li1):
    workbook=openpyxl.load_workbook('F:/cisco.xlsx')
    interface=workbook['interface']
    interface.append(li1)
    workbook.save('F:/cisco.xlsx')