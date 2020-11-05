# coding: utf-8


def adab(X_train, y_train, X_test, n_ets1, n_ets2):
	# 1.功能说明
	# 用Adaboost算法对X_train建模，输出数据集X_test上的模型预测结果，一个序列
	
	# 2.参数说明
	''' 
	:param X_train: 标准化，归一化后的数据集DataFrame
	:param y_train: 标准化，归一化后的数据集DataFrame
	:param X_test: 标准化，归一化后的数据集DataFrame
	:param n_ets1: 树的棵树，常用范围60-130
	:param n_ets2: 树的棵树，常用范围60-130
	:return: 一个序列
	''' 
	
	# 3.导包 
	from sklearn.ensemble import RandomForestRegressor   
  	from sklearn.ensemble import AdaBoostRegressor
	
	# 4.处理过程 
  	clf_adaboost_rand = AdaBoostRegressor(RandomForestRegressor(n_estimators=n_ets1), n_estimators=n_ets2, random_state=1)
	AdaBoost_rand = clf_adaboost_rand.fit(X_train, y_train.values.ravel())
	y_predict_AdaB_rand = AdaBoost_rand.predict(X_test)
	
	# 5.结果
  	return y_predict_AdaB_rand


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

n_ets1 = 95
n_ets2 = 100
result = adab(X_train, y_train, X_test, n_ets1, n_ets2)

# result：
'''
2020-08-01 00:00:00	57590.00
2020-09-01 00:00:00	61595.55
'''
