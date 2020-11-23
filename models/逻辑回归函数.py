def LR_model(Xtrain, ytrain, Xtest):
    # 1.函数功能说明
    # 应用线性回归算法对train_series训练建模，输出数据集X_test上的模型预测结果，一个序列
    
    # 2.参数说明 
    '''
	:param Xtrain: 训练特征数据集
	:param ytrain: 训练标签数据集
	:param Xtest: 测试特征数据集
    :return: 返回与Xtrain对应的预测值序列
    '''
    
    # 3.函数内部导包
    from sklearn.linear_model import LogisticRegression as LR
    
    # 4.处理过程
    LR = LinearRegression().fit(Xtrain, ytrain)
    print(LR.score(Xtrain, ytrain))
    yhat = LR.predict(Xtest)
    
    # 5.函数结果
    return yhat
    
########## 测试 #########    
# Xtrain
    '''
    P1	        P2	        P3        	P4         	P5	        P6
0	0.447386	0.343295	0.303571	0.242708	0.243063	0.224932	
1	0.000000	0.000000	0.000000	0.000000	0.000000	0.000000	
2	0.000000	0.000000	0.000000	0.000000	0.000000	0.000000	
3	0.036104	0.041740	0.040242	0.040160	0.074154	0.028819	
    

    '''
    # ytrain
    0        0
    1        1
    2        0
    3        0


    '''
    # X_test
    '''
    P1	        P2	        P3        	P4         	P5	        P6
0	0.063951	0.065151	0.065395	0.066063	0.065363	0.063803	
1	0.056306	0.059121	0.053623	0.072284	0.043975	0.051524
2	0.093502	0.180064	0.071585	0.164870	0.204843	0.158334
3	0.036104	0.041740	0.040242	0.040160	0.074154	0.028819
    '''
    
    # result = LR_model(Xtrain, ytrain, X_test)
    # result：
    '''
0        0
1        0
2        1
3        0
    '''
