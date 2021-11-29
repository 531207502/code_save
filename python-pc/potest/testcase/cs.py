import unittest
from ddt import ddt, data
from potest.pageobject.login_page import LoginPage
@ddt
class TestCase(unittest.TestCase):
    @data('软件测试','cyl')
    def test_01_login(self,n):
        cs = LoginPage()
        #cs.ysdx()
        cs.yxdl(n)