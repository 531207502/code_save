import pymysql
import time
def main():
    conn=pymysql.connect(host='cylcrystal.top',port=12345,user='root',password='890718feng',db='ljf_wxyd',charset='utf8')
    try:
        with conn.cursor() as cursor:
#里面的语句就按照mysql的操作语句来写
            nowtime=time.strftime("%Y_%m_%d", time.localtime())
            print(nowtime)
            sql_createTb = """CREATE TABLE %s  (
                             排名 INT ,
                             姓名  CHAR(20),
                             步数 INT
                             )
                             """% (nowtime)
            cursor.execute(sql_createTb)
            zd = {'张蓉':888,'czq':666,'cyl':444}
            keys=zd.keys()
            values=zd.values()
            list_key=list(keys)
            list_value=list(values)
            for i in range(len(zd)):
                key_value=list_key[i]
                value_value=list_value[i]
                print(key_value,value_value)
                result=cursor.execute('insert into %s values(%s,"%s",%s)'% (nowtime,i+1,key_value,value_value))
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
