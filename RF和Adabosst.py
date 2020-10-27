

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
		pass
	return df_ins
	
def normalization(df_ins):
	# 传入一个df，返回归一化后的df	
	from sklearn.preprocessing import minmax_scale
	df_ins = minmax_scale(df_ins)
	return df_ins
	

def call_RF(X_train, y_train, X_test, n_ets, max_d):
	# X_train 标准化，归一化后的训练集df
	# y_train 标准化，归一化后的训练集df
	# X_test 标准化，归一化后的测试集df
	# n_ets 常用范围60-130
	# max_d 常用范围7-25
	# 返回测试集上的预测结果，一个序列
	from sklearn.ensemble import RandomForestRegressor
    forest = RandomForestRegressor(n_estimators=n_ets, random_state=1, max_depth=max_d)
    Forest = forest.fit(X_train, y_train.values.ravel())
    y_predict_fore = Forest.predict(X_test)
	return y_predict_fore
	
	
def call_Ada_rand(X_train, y_train, X_test, n_ets1,n_ets2):
	# X_train 标准化，归一化后的训练集df
	# y_train 标准化，归一化后的训练集df
	# X_test 标准化，归一化后的测试集df
	# n_ets1 常用范围60-130
	# n_ets1 常用范围60-130
	# 返回测试集上的预测结果，一个序列
	from sklearn.ensemble import AdaBoostRegressor
	clf_adaboost_rand = AdaBoostRegressor(RandomForestRegressor(n_estimators=n_ets1), n_estimators=n_ets2, random_state=1)
    AdaBoost_rand = clf_adaboost_rand.fit(X_train, y_train.values.ravel())
    y_predict_AdaB_rand = AdaBoost_rand.predict(X_test)
	return y_predict_AdaB_rand









	
	
