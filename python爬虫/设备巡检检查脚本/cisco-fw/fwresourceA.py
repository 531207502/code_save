import re
def textcz(filename,textcount):
    print(filename)
    for i in range(len(textcount)-1):
        list1 = []
        result = re.search('(.*)(#|# )show resource usage', textcount[i])
        if result!=None:
            num = i+1
            list1.append(result.group(1))
            list1.append('\n')
            while(num):
                result1 = re.search('(#|# )show', textcount[num])
                if result1 ==None:
                    list1.append(textcount[num])
                    num+=1
                else:
                    num=0
        else:
            continue
        if list1!=None:
            with open('D:/xunjian/cisco-fw-resource.txt','a',encoding='utf-8') as  stream:
                stream.writelines(list1)
                stream.write('\n')