"""
logging模块

默认root日志收集器，默认输出级别WARING

日志名字
1、日志级别(level)：DEBUG、INFO、WARING、ERROR、CRITICAL（FATAL）
2、输出渠道(handel)：控制台(string_handle)、文件(file_handle)
3、日志内容（format）：时间-那个文件-哪行代码
"""

import logging

#创建自定义日志
#1、创建日志收集器
logger = logging.getLogger("maintain")

#2、设置日志获取级别
logger.setLevel(logging.INFO)

#3、设置日志输出渠道
handle1 = logging.StreamHandler()
# handle2 = logging.FileHandler()

#4、设置渠道输出格式
fmt = '%(asctime)s-第%(lineno)d行-%(name)s-%(filename)s-%(levelname)s-%(message)s'
formatter = logging.Formatter(fmt)

#5、将日志格式绑定到渠道中
handle1.setFormatter(formatter)
# handle2.setFormatter(formatter)

#6、将设置好的渠道添加到日志收集器中
logger.addHandler(handle1)

logger.error("第一个")