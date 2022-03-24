
#读取
#os.getcwd()获取当前路径
#mode= r 读 a 增量写入 w 写
import os

import yaml


def read_yaml():
    with open(os.getcwd()+'yaml文件路径',mode='r',encoding='utf-8') as f:
        value=yaml.load(stream=f,loader=yaml.FullLoader)
        return value
#写入
def write_yaml(data):
    with open(os.getcwd()+'yaml文件路径',mode='a',encoding='utf-8') as f:
        yaml.dump(data,stream=f,allow_unicode=True)

#清空
def clear_yaml(data):
    with open(os.getcwd()+'yaml文件路径',mode='w',encoding='utf-8') as f:
      f.truncate()