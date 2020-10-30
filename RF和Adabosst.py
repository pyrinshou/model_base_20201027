

def standard(df_ins, s_type='ftf'):
	# s_type='ftf' ，基于均值和方差将训练数据转为标准正态分布
	# s_type='tf'  ，直接将训练数据转为标准正态分布
	# 传入一个df，返回标准化后的df
	from sklearn.preprocessing import StandardScaler 
	scaler = StandardScaler()
	if s_type='ftf': 
		df_ins = scaler.fit_transform(df_ins)
	elif s_type='tf': 
		df_ins = scaler.transform(df_ins)
	else:
		df_ins = None
	return df_ins
	
def normalization(df_ins):
	# 传入一个df，返回归一化后的df	
	from sklearn.preprocessing import minmax_scale
	df_ins = minmax_scale(df_ins)
	return df_ins
	

def call_RF(X_train, y_train, X_test, n_ets, max_d):
	'''
	:： 应用随机森林算法，对训练集数据建模并对测试集数据进行验证，返回一个格式为series的预测结果
	:param X_train： 标准化，归一化后的训练集df
	:param y_train: 标准化，归一化后的训练集df
	:param X_test: 标准化，归一化后的测试集df
	:param n_ets: 树的数量，常用范围60-130
	:param max_d: 树的深度，常用范围7-25
	:return: 返回测试集上的基于随机森林算法预测结果，一个序列
	'''
	from sklearn.ensemble import RandomForestRegressor
        forest = RandomForestRegressor(n_estimators=n_ets, random_state=1, max_depth=max_d)
        Forest = forest.fit(X_train, y_train.values.ravel())
        y_predict_fore = Forest.predict(X_test)
	return y_predict_fore
	
	
def call_Ada_rand(X_train, y_train, X_test, n_ets1,n_ets2):
	'''
	:param X_train： 标准化，归一化后的训练集df
	:param y_train: 标准化，归一化后的训练集df
	:param X_test: 标准化，归一化后的测试集df
	:param n_ets1: 树的数量，常用范围60-130
	:param n_ets2: 树的数量，常用范围60-130
	:return:  返回测试集上的基于Adaboost算法预测结果，一个序列
	'''
	from sklearn.ensemble import AdaBoostRegressor
	clf_adaboost_rand = AdaBoostRegressor(RandomForestRegressor(n_estimators=n_ets1), n_estimators=n_ets2, random_state=1)
        AdaBoost_rand = clf_adaboost_rand.fit(X_train, y_train.values.ravel())
        y_predict_AdaB_rand = AdaBoost_rand.predict(X_test)
	return y_predict_AdaB_rand

def pridict_by_arimax(train_series, test_series, num):
    '''
    :param train_series: 训练集序列
    :param test_series: 测试集序列
    :param num: 预测期数
    :return: 返回一个预测的结果序列
    '''
    one_model = sm.tsa.statespace.SARIMAX(train_series, order=(1,1,1), seasonal_order=(1,1,1,12),enforce_stationarity=False, enforce_invertibility=False).fit(disp=-1)
    pre_val = one_model.forecast(steps=num, exog=test_series)
    return pre_val[0]

def pridict_by_arimax2(train_x_series, train_y_series, test_x_series, num):
    '''
    :param train_x_series: 训练集特征序列
    :param train_y_series: 训练集目标值序列
    :param test_x_series: 测试集序列
    :param num: 预测期数
    :return: 返回一个预测的结果序列
    '''
    # train_x_series ---->Series or DataFrame
    # train_y_series ---->Series  与 train_x_series 对应
    # test_x_series ---->Series or DataFrame  与num 对应
    # num ----> 结果期数
#     one_model = sm.tsa.statespace.SARIMAX(train_y_series, exog=train_x_series, order=(1,1,1), seasonal_order=(1,1,1,12),enforce_stationarity=False, enforce_invertibility=False).fit(disp=-1)
    one_model = sm.tsa.statespace.SARIMAX(train_y_series, exog=train_x_series).fit(disp=-1)
    pre_val = one_model.forecast(steps=num, exog=test_x_series)
    return pre_val[0]







	
	
