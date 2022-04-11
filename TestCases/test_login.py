import unittest
from Common.handle_requests import send_requests
from Common.handle_excel import HandleExcel
import os
from Common.handle_path import datas_dir
from my_loger import mtlogger

#获取当前测试数据
he = HandleExcel(os.path.join(datas_dir+"\\login_datas.xlsx"), "login")
cases = he.read_datas()
he.close_file()
#编写测试用例


class TestLogin(unittest.TestCase):

    def test_login_ok(self):
        case = cases[0]
        expected = eval(case["expected"])
        #步骤（测试数据-发起请求)
        try:
            sq = send_requests(case["method"], case["url"], case["request_data"])
        #断言
            self.assertEqual(sq.json()["code"], expected["code"])
            self.assertEqual(sq.json()["msg"], expected["msg"])
        except AssertionError:
            mtlogger.exception("获取验证码失败，请确认数据")
        else:
            mtlogger.info("获取验证码成功")


