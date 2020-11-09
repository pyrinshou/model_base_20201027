# coding: utf-8

def rf(X_train, y_train, X_test, n_ets, max_d):
	# 1.功能说明
	# 用随机森林算法对X_train建模，输出数据集X_test上的模型预测结果，一个序列
	
	# 2.参数说明
	''' 
	:param X_train: 标准化，归一化后的数据集df
	:param y_train: 标准化，归一化后的数据集df
	:param X_test: 标准化，归一化后的数据集df
	:param n_ets: 树的棵树，常用范围60-130
	:param max_d: 树的深度，常用范围7-25
	:return: 一个序列
	''' 
	
	# 3.导包 
	from sklearn.ensemble import RandomForestRegressor   
	
	# 4.处理过程 
  	forest = RandomForestRegressor(n_estimators=n_ets, random_state=1, max_depth=max_d)
    	Forest = forest.fit(X_train, y_train.values.ravel())
    	y_predict_fore = Forest.predict(X_test)
	
	# 5.结果
  	return y_predict_fore


########## 测试 #########

# X_train
	'''
	2019-12-01	2927.823096	2596.640400
	2020-05-01	2856.270300	2584.855247
	'''
# y_train
'''
	2019-12-01    52590.00
	2020-05-01    62585.55
'''
# X_test
	'''
	2020-08-01 00:00:00	1886.710000	2126.140000
	2020-09-01 00:00:00	1836.780000	1758.400000
	'''

n_ets = 95
max_d = 8
result = rf(X_train, y_train, X_test, n_ets, max_d)

# result：
'''
2020-08-01 00:00:00	57590.00
2020-09-01 00:00:00	61595.55
'''
