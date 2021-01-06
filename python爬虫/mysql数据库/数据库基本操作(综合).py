import pymysql
def main():
    conn=pymysql.connect(host='wp35776584.qicp.vip',port=12345,user='root',password='890718feng',charset='utf8')
    with conn.cursor() as cursor:
        cz=1
if __name__ == '__main__':
 main()
