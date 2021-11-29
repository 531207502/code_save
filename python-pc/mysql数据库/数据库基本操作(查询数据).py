import pymysql
def main():
    conn=pymysql.connect(host='192.168.0.150',port=3306,user='root',password='890718feng',db='sjk_test',charset='utf8')
    try:
        with conn.cursor() as cursor:
            cursor.execute('select teaid,teaname,teatitle from tb_teacher')
            for row in cursor.fetchall():
                print(row)
    except pymysql.MySQLError as error:
        print(error)
        conn.rollback()
    finally:
        conn.close()
if __name__ == '__main__':
    main()
