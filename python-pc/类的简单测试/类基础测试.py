# 1、创建Person类，属性有姓名、年龄、性别，创建方法personInfo,打印这个人的信息
# 2、创建Student类，继承Person类，属性有学院college
# ，班级class，重写父类personInfo方法，调用父类方法打印个人信息外，将学生的学院、班级信息也打印出来，
# 创建方法study参数为Teacher对象，调用Teacher类的teachObj方法，接收老师教授的知识点，然后打印‘老师xxx,我终于学会了！’xxx为老师的teach方法返回的信息。
# 重写__str__方法，返回student的信息。
# 3、创建Teacher类，继承Person类，属性有学院college，专业professional
# ，重写父类personInfo方法，调用父类方法打印个人信息外，将老师的学院、专业信息也打印出来。
# 创建teachObj方法，返回信息为‘今天讲了如何用面向对象设计程序’
# 4、创建三个学生对象，分别打印其详细信息
# 5、创建一个老师对象，打印其详细信息
# 6、学生对象调用learn方法
class Person:
    def __init__(self,name,age,sex):
        print('这个打印的是init里面的东西')
        self.name=name
        self.age=age
        self.sex=sex
    def personInfo(self):
        print("姓名是{}，年龄是{}，性别是{}".format(self.name,self.age,self.sex))
class Student(Person):
    def __init__(self,name,age,sex,college,banji):
        super().__init__(name,age,sex)
        self.college=college
        self.banji=banji
    def personInfo(self):
        print("我叫{}，年龄是{}，性别是{}，所在学院{}，所在班级{}".format(self.name,self.age,self.sex,self.college,self.banji))
    def study(self,teacher):
        print("我的名字是{},老师{}，我终于学会了！".format(self.name,teacher.teachObj()))
    def __str__(self):
        msg="我叫{},年龄是{}，性别是{}，所在学院是{}，所在班级是{}".format(self.name,self.age,self.sex,self.college,self.banji)
        return msg
class Teacher(Person):
    def __init__(self,name,age,sex,college,professional):
        super().__init__(name, age, sex)
        self.college=college
        self.professional=professional
    def personInfo(self):
        print("老师姓名是{},年龄是{}，性别是{}，老师学院是{}，所属专业是{}".format(self.name,self.age,self.sex,self.college,self.professional))
    def teachObj(self):
        msg="今天讲了如何用面向对象设计程序"
        return msg
# student1=Person("张三",19,"男")
# student1.personInfo()
# student2=Person("韩梅梅",16,"女")
# student2.personInfo()
# student3=Person("李雷",21,"男")
# student3.personInfo()
# teacher1=Teacher("李时文","27","男","H3C学院","h3cie")
# teacher1.personInfo()
# student4=Student("张三",19,"男","cisco","ccie")
# student4.study(teacher1)
# student5=Student("韩梅梅",16,"女","h3c","hcie")
# student5.study(teacher1)
# student6=Student("李雷",21,"男","hw","hwie")
# student6.study(teacher1)
per1=Person('l','28','nan')