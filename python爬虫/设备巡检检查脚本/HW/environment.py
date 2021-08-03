import re
def textcz(filename,textcount):
    print(filename)
    for i in range(len(textcount)-1):
        list1 = []
        result1 = re.search('>display fan', textcount[i])
        result2 = re.search('>display power$', textcount[i])
        result8 = re.search('>display power system', textcount[i])
        result3 = re.search('>display health', textcount[i])
        if result1:
            num = i+1
            list1.append(result1.group(0)[1:])
            list1.append('\n')
            while(num):
                result4 = re.search('>display', textcount[num])
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
                result4 = re.search('>display', textcount[num])
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
                result4 = re.search('>display', textcount[num])
                if result4 ==None:
                    list1.append(textcount[num])
                    num+=1
                else:
                    num=0
        elif result8:
            num = i+1
            list1.append(result8.group(0)[1:])
            list1.append('\n')
            while(num):
                result4 = re.search('>display', textcount[num])
                if result4 ==None:
                    list1.append(textcount[num])
                    num+=1
                else:
                    num=0
        else:
            continue
        if list1:
            with open('D:/xunjian/hw env.txt','a',encoding='utf-8') as  stream:
                stream.write(filename)
                stream.write('\n')
                stream.writelines(list1)