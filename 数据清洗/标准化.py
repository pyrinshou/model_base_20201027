# coding: utf-8

def standard(df_ins, s_type='ftf'):
	  # 1.功能说明
    # 用随机森林算法对X_train建模，输出数据集X_test上的模型预测结果，一个序列

    # 2.参数说明
    ''' 
    :param df_ins: DataFrame格式的数据集df
    :param s_type:  s_type='ftf' 基于均值和方差将训练数据转为标准正态分布
            s_type='tf'，直接将训练数据转为标准正态分布
    :return: 返回标准化后的array
    '''
    from sklearn.preprocessing import StandardScaler 

    scaler = StandardScaler()
    if s_type='ftf': 
      df_ins = scaler.fit_transform(df_ins)
    elif s_type='tf': 
      df_ins = scaler.transform(df_ins)
    else:
      df_ins = None
    return df_ins
  
  
########## 测试 #########    
# df
	'''
	58590.00 52490.00
	62585.55 66290.00
	'''

df_ins = df
num = 2
result = standard(df_ins, s_type='ftf')

# result：
'''
[[1.38061899,  0.90269005],[0.88383094, 0.11112092,]]
'''
