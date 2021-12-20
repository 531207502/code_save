import unittest
from HTMLTestRunner import HTMLTestRunner
if __name__ == '__main__':
    #执行需要的用例，并生成报告
    #使用unittest下默认的测试用例加载器去发现testcase目录下名为chaxun.py的文件
    suite = unittest.defaultTestLoader.discover("./testcase","chaxun.py")
    #生成报告文件
    report_file =open("./report/reports.html","wb")
    #生成一个htmltestrunner对象（必须下载一个htmltestrunner文件放到python lib目录下）
    runner = HTMLTestRunner(stream=report_file, title='test', description='登陆测试')
    #通过运行器运行测试用例
    runner.run(suite)
    report_file.close()