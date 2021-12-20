from ddt import ddt, data
from TBpotest.base.base_util import BaseUtil
from TBpotest.pageobject.chaxun import chaxunPage
from TBpotest.pageobject.login_page import LoginPage
@ddt
class TestCase(BaseUtil):
    '''最外面的查询'''
    @data('汽车','矿泉水')
    def test_02_chaxun(self,args):
        '''查询测试'''
        test = chaxunPage(self.driver)
        test.user_chaxun(args)