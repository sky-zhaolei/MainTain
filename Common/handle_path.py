"""
全局路径设置
"""

import os

Base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(Base_dir)
#测试用例路径
cases_dir = os.path.join(Base_dir, "TestCases")

#测试数据路径
datas_dir = os.path.join(Base_dir, "TestDatas")
print(datas_dir)
#输出测试报告路径
reports_dir = os.path.join(Base_dir, "Outputs\\reports")

#日志路径
logs_dir = os.path.join(Base_dir, "TestCases\\logs")

#配置路径
conf_dir = os.path.join(Base_dir, "Conf")

