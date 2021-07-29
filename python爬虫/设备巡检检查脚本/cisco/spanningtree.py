import re
import openpyxl
global count1
def textcz(filename,textcount):
    for i in range(len(textcount)+1):
        result=re.search('(.*)(#|# )show (spanning-tree$|spanning-tree brief$)',textcount[i])
        if result:
            count1=i
            break
        else:
            continue
    num=1
    count1+=1
    list0=[]
    print(count1)
    print(len(textcount))
    while(num):
        result1 = re.search('(.*)(#|# )show ', textcount[count1])
        result2 = re.search('(^VLAN(\d)+)|(^MST(\d)+)',textcount[count1])
        if result1:
           list0.append(result1.group(1))
           list0.append('---------------------')
           list0.append('---------------------')
           list0.append('------END------')
           list0.append('---------------------')
           list0.append('---------------')
           writeexcel(list0)
           break
        elif result2:
            list1=[]
            bl2=1
            while(bl2):
                count1+=1
                #print('zuineiceng',count1)
                result3 = re.search('Root ID +Priority +((\d)+)',textcount[count1])
                result4 = re.search('Bridge ID +Priority +((\d)+)',textcount[count1])
                result7 = re.search(
                    '(^(\w)+/(\d)+)(\s)+([a-zA-Z]+)(\s)+([A-Z]+)(\s)+(\d)+(\s)+(\d)+\.(\d)+(\s)+(.*)',
                    textcount[count1])
                result10 = re.search(
                    '(^(\w)+ )(\s)+([a-zA-Z]+)(\s)+([A-Z]+)(\s)+(\d)+(\s)+(\d)+\.(\d)+(\s)+(.*)',
                    textcount[count1])
                result8 = re.search('^MST(\d)+|^VLAN(\d)+',textcount[count1])
                result9 = re.search('(.*)(#|# )show ', textcount[count1])
                if result8 or result9:
                    #print('zhengeshakajkdsads')
                    #count1+=1
                    break
                elif result3:
                    result5 = re.search('Address +(.*)',textcount[count1+1])
                    list1.append(result.group(1))
                    if result2.group(1)==None:
                        list1.append(result2.group(3))
                    else:
                        list1.append(result2.group(1))
                    resultbd5=result5.group(1)
                    list1.append(result3.group(1))
                    list1.append(result5.group(1))
                    continue
                elif result4:
                    result6 = re.search('Address +(.*)', textcount[count1+1])
                    list1.append(result4.group(1))
                    list1.append(result6.group(1))
                    #print(list1)
                    resultbd6 = result6.group(1)
                    if resultbd5==resultbd6:
                        list1.append('此设备为根桥')
                    writeexcel(list1)
                    continue
                elif result7:
                    list2=[]
                    list2.append(result.group(1))
                    list2.append(result7.group(1))
                    list2.append(result7.group(5))
                    list2.append(result7.group(7))
                    list2.append(result7.group(14))
                    writeexcel(list2)
                    continue
                elif result10:
                    list2=[]
                    list2.append(result.group(1))
                    list2.append(result10.group(1))
                    list2.append(result10.group(4))
                    list2.append(result10.group(6))
                    list2.append(result10.group(13))
                    writeexcel(list2)
                    continue
                else:
                    continue
        else:
            count1+=1
            #print('zhegeshishenme',count1)
def writeexcel(li1):
    workbook=openpyxl.load_workbook('D:/xunjian/cisco-st.xlsx')
    memory1=workbook['spanning-tree']
    memory1.append(li1)
    workbook.save('D:/xunjian/cisco-st.xlsx')
