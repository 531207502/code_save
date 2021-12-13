import pymysql
def main():
    conn=pymysql.connect(host='192.168.0.150',port=3306,user='root',password='890718feng',db='sjk_test',charset='utf8')
    try:
        with conn.cursor() as cursor:
#里面的语句就按照mysql的操作语句来写
            result=cursor.execute('insert into tb_teacher values(4488,"程征求","校长","3")')
#这里的返回值是操作后影响的行，这里就添加了一行所以返回的是1
            if result==1:
                print("添加数据成功")
#使用游标进行数据更改时必须确认提交才生效
                conn.commit()
#如果添加失败或者操作有误，要进行回滚
    except pymysql.MySQLError as error:
        print(error)
        conn.rollback()
    finally:
        conn.close()
if __name__ == '__main__':
    main()