#!/usr/bin/env python
# coding: utf-8

# In[16]:


def geoget(df):
    
    '''
    1.功能说明:
    获取地址的经纬度

    2.参数说明
    :param df: 传入一个DataFrame格式的数据集
    
    ''' 
   # 3.导包

    import requests
    import time
    import pandas as pd
    
    #4.处理过程
    for index, row in df.iterrows():
        url = 'http://api.map.baidu.com/geocoder/v2/?address=%s&output=json&ak=APGB5LA9p7cO9B70lZfSTYZYTgqfcLEt&callback=showLocation' % (row['地址'])
        response = requests.get(url)
        loc = eval(response.text.split("&&")[1].replace(")","").replace("showLocation(",""))
        row['经度'] = str(loc['result']['location']['lng'])
        row['纬度'] =  str(loc['result']['location']['lat'])
    return df

########## 测试 #########
'''
address
地址              经度        纬度
三明市梅列区
三明市三元区
三明市永安市
三明市沙县
三明市尤溪县
三明市大田县
三明市明溪县
三明市清流县
三明市宁化县
三明市将乐县
三明市泰宁县
三明市建宁县
'''

address = pd.read_excel('./address_test.xls',encoding='gbk')
address = geoget(address)
address.to_excel('./address_result.xls',index=None)

'''
结果
    地址                经度                纬度
三明市梅列区     117.65255022877358   26.277335878354766
三明市三元区     117.61441509378494   26.24021937457406
三明市永安市     117.37144258732353   25.948143989823954
三明市沙县       117.79856107580882   26.40281344434632
三明市尤溪县     118.19743971364737   26.176218039460192
三明市大田县     117.85343999668406   25.698932641878844
三明市明溪县     117.20851763567705   26.361853685276866
三明市清流县     116.82359318579535   26.183357353210287
三明市宁化县     116.66042551200016   26.267956490540477
三明市将乐县     117.47740904083985   26.735209519833294
三明市泰宁县     117.18259586239803   26.90566003228466
三明市建宁县     116.85250622659105   26.83682465534918

'''

