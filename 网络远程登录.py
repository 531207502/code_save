import telnetlib
import time
import re
host="220.167.54.88"
tn=telnetlib.Telnet(host=host,port=23,timeout=30)
tn.set_debuglevel(2)
tn.read_until(b"login:")
tn.write("wenxuan".encode("utf-8")+b"\n")
tn.read_until(b"Password:")
tn.write("bsqt75wmc".encode(("utf-8"))+b"\n")
tn.read_until(b"<Center_MSR36_1>")
tn.write("display curr".encode(("utf-8"))+b"\n")
time.sleep(2)
list1=[]
#result=tn.read_very_eager().decode("utf-8")
#result1=re.sub(r"\r\n",r"\n",result)
with open("txt.txt","w",encoding="utf-8",newline="") as fp:
    #fp.write(result1)
    while(True):
        result=tn.read_very_eager().decode("utf-8")
        result1=re.sub(r"\r\n",r"\n",result)
        if "---- More ----" in result1.strip():
            result2=re.sub(r"---- More ----","",result1)
            result3 = re.sub("\\r\\r\\s*\\r","", result2)
            tn.write(b" ")
            time.sleep(0.5)
        else:
            break
        list1.append(result3)
    cd=len(list1)
    for i in range(cd):
        fp.write(list1[i])
