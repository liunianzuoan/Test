import logging
import logging.handlers
from common import contants
from common.read_conf import ReadConfig
import os
config = ReadConfig()

# 存入一个日志收集器
def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel('DEBUG')   # 定义日志收集的级别

        # 定义一个日志输出的格式
    fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s - [%(filename)s:%(lineno)s]"
    formate = logging.Formatter(fmt)   # 控制台输出格式

        # 定义指定的文件来输出
    log_name = os.path.join(contants.logs_dir,'case.log')
    file_handler = logging.handlers.RotatingFileHandler(log_name,maxBytes=20*1024*1024,backupCount =10,
    encoding = 'UTF-8')
    level= config.get_value('log','file_handler')
    file_handler.setLevel(level)   #设置文件日志输出的级别
    file_handler.setFormatter(formate)   #设置文件日志输出的格式

      # 控制台输出
    console_handler =logging.StreamHandler()
    level =config.get_value('log','console_handler')
    console_handler.setLevel(level)
    console_handler.setFormatter(formate)

        #添加
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger

logger = get_logger(logger_name='invest')
if __name__ == '__main__':
    logger.error('我是一条error错误信息')
    logger.critical('我是一个严重bug')




# 输出到文件，文件路径请使用绝对路径 logs
# 输出控制台，定义输出级别debug
# 不同的输出级别可配置


