import unittest
import os
from BeautifulReport import BeautifulReport
from Common.handle_path import cases_dir,reports_dir


#收集用例
s = unittest.TestLoader.discover(cases_dir)

#生成测试报告
br = BeautifulReport(s)
br.report("maintain造数据自动化",reports_dir + "\\report.html")