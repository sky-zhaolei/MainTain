import logging
from logging import Logger

class Mylogger(Logger):

    def __init__(self, name, leave=logging.INFO, file=None):
        #设置输出级别、输出渠道、日志格式
        super().__init__(name, leave)

        #设置渠道输出格式
        fmt = '%(asctime)s-%(name)s-%(filename)s-第%(lineno)d行-%(levelname)s-%(message)s'
        formatter = logging.Formatter(fmt)

        #设置控制台渠道
        handle1 = logging.StreamHandler()
        handle1.setFormatter(formatter)
        self.addHandler(handle1)

        #判断是否需要文件输出渠道
        if file:
            # 设置文件渠道
            handle2 = logging.FileHandler(file, encoding="utf-8")
            handle2.setFormatter(formatter)
            self.addHandler(handle2)

mtlogger = Mylogger("MT", file="mylo.log")
if __name__ == '__main__':
    pass