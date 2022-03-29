import unittest
from Common.handle_requests import send_requests

"""
定义测试类，继承unittest.TestCases
在测试类中，以test_开头，定义测试函数
每一个test_开头的函数，就是一个测试用例
编写用例：
    1、测试数据
    2、测试步骤
    3、预期结果与实际结果的比对（断言）

"""

class TestLogin(unittest.TestCase):

    def test_get_vincode(self):    #获取验证码
        url = "http://store.test.dstcar.com/dst-partner-apis/api-store/public/verifyCode"
        datas = {"phone":"15070720246"}
        res = send_requests("POST",url,datas)
        print(res.json())
        assert res.json()["code"] == 200

        pass

    # def test_login_ok(self):  #登录
    #     res = send_requests()
    #     pass



