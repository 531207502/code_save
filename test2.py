import pymysql
conn = pymysql.connect(host="localhost",user="root",password="root",database="mysql_test",port=3306)
#cursor =  conn.cursor()
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# sql="""
# insert into aa(id,name,salary) values(null,%s,%s)
# """
# namelist=["test1","test2","test3"]
# salarylist=[3000,4000,5000]
# for i in range(3):
#     name=namelist[i]
#     salary=salarylist[i]
#     cursor.execute(sql,(name,salary))
# conn.commit()
sql="""
select * from aa
"""
cursor.execute(sql)
result= cursor.fetchall()
print(result)
print(len(result))
conn.close()

