import re
def textcz(filename,textcount):
    print(filename)
    for i in range(len(textcount)-1):
        list1 = []
        result1 = re.search('#show environment', textcount[i])
        result2 = re.search('#show system power', textcount[i])
        result3 = re.search('#show system fan', textcount[i])
        if result1:
            num = i+1
            list1.append(result1.group(0)[1:])
            list1.append('\n')
            while(num):
                result4 = re.search('#show', textcount[num])
                if result4 ==None:
                    list1.append(textcount[num])
                    num+=1
                else:
                    num=0
        elif result2:
            num = i+1
            list1.append(result2.group(0)[1:])
            list1.append('\n')
            while(num):
                result4 = re.search('#show', textcount[num])
                if result4 ==None:
                    list1.append(textcount[num])
                    num+=1
                else:
                    num=0
        elif result3:
            num = i+1
            list1.append(result3.group(0)[1:])
            list1.append('\n')
            while(num):
                result4 = re.search('#show', textcount[num])
                if result4 ==None:
                    list1.append(textcount[num])
                    num+=1
                else:
                    num=0
        else:
            continue
        if list1:
            with open('D:/xunjian/mp env.txt','a',encoding='utf-8') as  stream:
                stream.write(filename)
                stream.write('\n')
                stream.writelines(list1)