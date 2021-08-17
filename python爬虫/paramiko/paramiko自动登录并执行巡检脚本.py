import paramiko
import time
import re
import os
# 建立一个sshclient对象
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#遍历需要保存配置的设备信息，并根据对应信息进行登录操作
with open('D:/xunjian/savetest/information.txt', 'r', encoding='gbk') as  stream1:
    #获取每一行的数据，放在一个列表中
    list1 = stream1.readlines()
    # 获取行数,实际就是要巡检的设备数
    length = len(list1)
    #创建一个文件并加上本地时间戳，精确到日
    os.mkdir('D:/xunjian/savetest/' + time.strftime("%Y-%m-%d", time.localtime()))
    for count in range(length):
        nr=list1[count]
        qpresult=nr.split(',')
        qpcount=len(qpresult)
        ssh.connect(hostname=qpresult[1], port=22, username=qpresult[2], password=qpresult[3],allow_agent=False,look_for_keys=False)
        conn = ssh.invoke_shell()
        for bl in range(4,qpcount):
            conn.send(qpresult[bl]+'\n')
            time.sleep(0.5)
        with open('D:/xunjian/savetest/mingling.txt', 'r', encoding='utf-8') as  stream2:
            list2 = stream2.readlines()
            stream2.seek(0)
            length2 = len(stream2.readlines())
            for count2 in range(length2):
                conn.send(list2[count2]+'\n')
                time.sleep(0.5)
            out = conn.recv(65536*65536)
            fp1=open('D:/xunjian/savetest/'+time.strftime("%Y-%m-%d", time.localtime())+'/'+qpresult[0]+'.txt','w',encoding='utf-8')
            fp1.writelines(out.decode('utf-8').replace('\r\n','\n'))
            fp1.close()
            ssh.close()