class Test:
    __age=18
    @classmethod
    def test(cls,n):
        cls.__age+=n
        print("现在实际的年龄是：{}".format(cls.__age))
    def ff(self,n):
        self.__age+=n
        print("ff里面的年龄是:{}".format(self.__age))
Test.test(3)
test1=Test()
test1.ff(100)