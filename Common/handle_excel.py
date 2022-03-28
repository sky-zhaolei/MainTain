"""
excel类的需求是什么
1、读取表头
2、读取数据 - 读取表头以外的所有数据，返回值：列表  成员是每一行数据

初始化工作    加载excel文件，打开一个表单
"""
from openpyxl import load_workbook
import json


class HandleExcel:
    def __init__(self, file_path, sheet_name):
        # 1、加载excel数据文件
        self.wb = load_workbook(file_path)
        # 2\读取对应的表单
        self.sh = self.wb[sheet_name]

    def read_titles(self):
        # 获取首行字段名称值，即字典key值
        titles = []  # 定义一个列表，用于存储首行的数据
        for item in list(self.sh.rows)[0]:
            titles.append(item.value)  # 将获取到的首行，加入到titles列表
        return titles

    def read_datas(self):       #读取所有数据函数
        all_datas = []  #定义一个列表，用于存储读取后的数据
        titles = self.read_titles()
        for item in list(self.sh.rows)[1:]:
            value_dict = []  # 每一行是个新字典
            for index in item:
                value_dict.append(index.value)  # 将读取到的每一行值添加入value_dict列表
            res = dict(zip(titles, value_dict))  # 将titles和读取出的每行数据，均打包成字典,使用dict方法转换成字典
            #res["check"] = eval(res["check"])  # 在追加到列表中时，将check行转换为字符对象
            res["request_data"] = json.loads(res["request_data"])#将请求数据从json字符串转换成字典
            all_datas.append(res)  # 将每一行字段均追加到data_lists列表中
        return all_datas

    def close_file(self):
        self.wb.close()


if __name__ == '__main__':
    import os
    # 获取数据当前目录下的测试数据文件
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../TestDatas/login_datas.xlsx")
    exc = HandleExcel(file_path, "login")
    datas = exc.read_datas()
    exc.close_file()

