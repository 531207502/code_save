from TBpotest.base.base_util import BaseUtil
from TBpotest.pageobject.chaxun import chaxunPage
from TBpotest.pageobject.login_page import LoginPage
class TestCase(BaseUtil):
    def test_01_login(self):
        test=LoginPage(self.driver)
        test.user_login()