import time
from pyVim.connect import SmartConnectNoSSL
import atexit
import argparse

def denglu(ip, user, passwd, port):
    try:
        client = SmartConnectNoSSL(host=ip,
                                   user=user,
                                   pwd=passwd,
                                   port=port
                                   )
        content = client.RetrieveContent()
        return content
    except Exception as e:
        print("登录参数存在问题")
if __name__ == '__main__':
    ip = '10.10.1.2'
    user = 'administrator@vsphere.local'
    password = 'VMware1!'
    port = 443
    result=denglu(ip,user,password,port)
    print(result)
    hosts = result.viewManager
    print(type(hosts))