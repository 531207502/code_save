import re
global count
def textcz(filename,textcount):
    print(filename)
    list1 = []
    count=1
    for i in range(len(textcount)-1):
        result = re.search('(.*)(#|# )show context detail', textcount[i])
        if result:
            num = i+1
            while(num):
                result1 = re.search('(#|# )', textcount[num])
                result2 = re.search('Context "(.*)"',textcount[num])
                if result1 ==None and result2 == None:
                    num+=1
                elif result2:
                    list1.append(result2.group(1))
                    num+=1
                elif result1:
                    num=0
                    count=0
                else:
                    num+=1
        elif count==0:
            break
        else:
            continue
        return list1
