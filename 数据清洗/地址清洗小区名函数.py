# coding: utf-8

def get_XQ(str1):
    # 1.功能说明
    # 从地址格式的字符串中清洗出所包含的小区名称

    # 2.参数说明
    ''' 
    :param str1: 地址字符串
    ''' 
    
    # 3.导包 
    import pandas as pd
    import numpy as np
    import re

    # 4.处理过程 
    str1 = str1.split('(', 1)[0]
    str1 = str1.split('（', 1)[0]
    str1 = str1.split('[', 1)[0]
    str1 = str1.split('县', 1)[-1]
    if '镇' in str1 and '小镇' not in str1:
        str1 = str1.split('镇', 1)[-1]
    if '路' in str1 and '路口' not in str1 and '路边' not in str1:
        str1 = str1.split('路')[-1]
    str1 = str1.split('街道')[-1]
    str1 = str1.split('街',1)[-1]
    str1 = str1.split('道',1)[-1]
    str1 = str1.split('巷',1)[-1]
    str1 = str1.split('村委会', 1)[-1]
    str1 = str1.split('居委会', 1)[-1]
    str1 = str1.split('委员会', 1)[-1]
    str1 = str1.split('号楼', 1)[0]
    str1 = str1.split('座', 1)[0]
    str1 = str1.split('幢', 1)[0]
    str1 = str1.split('栋', 1)[0]
    str1 = str1.split('楼', 1)[0]
    str1 = str1.split('单元', 1)[0]
    str1 = str1.split('地下室', 1)[0]
    str1 = str1.split('#')[0]
    str1 = str1.split('-', 1)[0]
    for i in range(1,10):
        str1 = str1.split(str(i)+'区', 1)[0]
    for i in ['一','二','三','四','五','六','七','八','九','东','西','南','北']:
        str1 = str1.split(i+'区', 1)[0]
    str1 = re.sub(r'\d+'+'室', '',str1)
    str1 = re.sub(r'\d+', '',str1)
    str1 = re.split(r'[a-zA-Z]',str1)[0]
    str1 = str1.strip(r'-').strip(r'(').strip(r')').strip('号').strip('*').strip()
    str1 = str1.split('号', 1)[-1]

    # 5.结果
    return str1


########## 测试 #########

    # xq
    '''
    '福州市鼓楼区湖东路155号锦绣佳园'
    '''
    str1 = xq

    XQ = get_XQ(xq)

    # XQ结果为
    '''
    '锦绣佳园'
    '''
