## 模型上传标准：

def pridict_by_arimax(train_series, test_series, num):
    # 1.函数功能说明
    # 应用arimax算法对train_series训练建模，以该模型对test_series的num个目标期数据进行预测
    
    # 2.参数说明 
    '''
    :param train_series: 训练数据集
    :param test_series: 测试数据集
    :param num: 预测期数
    :return: 返回与test_series对应的预测值序列
    '''
    
    # 3.函数内部导包
    import statsmodels.api as sm
    
    # 4.处理过程
    one_model = sm.tsa.statespace.SARIMAX(train_series, order=(1,1,1), seasonal_order=(1,1,1,12),enforce_stationarity=False, enforce_invertibility=False).fit(disp=-1)
    pre_val = one_model.forecast(steps=num, exog=test_series)
    
    # 5.函数结果
    return pre_val[0]



########## 测试 #########    
# train_series
	'''
	2019-12-01	52590.00
	2020-01-01	62585.55
	'''
# test_series
	'''
	2020-02-01 00:00:00	np.nan
	2020-03-01 00:00:00	np.nan
	'''
num = 2
result = pridict_by_arimax(train_series, test_series, num)

# result：
'''
2020-02-01 00:00:00	57590.00
2020-03-01 00:00:00	61595.55
'''
