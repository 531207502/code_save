import pymysql
def main():
    conn=pymysql.connect(host='192.168.0.150',port=3306,user='root',password='890718feng',db='sjk_test',charset='utf8')
    try:
        with conn.cursor() as cursor:
            teaid=input("请输入你要删除的教师编号：")
#这里的语句注意，为什么后面是跟的元组，可以ctrl+左键来看execute这个函数的说明
            result=cursor.execute('delete from tb_teacher where teaid=%s',(teaid,))
            if result==1:
                print("删除数据成功")
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
