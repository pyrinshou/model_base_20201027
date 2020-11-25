
# 基础聚类函数（包括归一化、聚类标签、聚类中心）
def my_kmeans(df, k=3, start_col=None, end_col=None):
    #1.函数功能说明
    #应用基础聚类函数k-means
    
    #2.参数说明
    '''
    df:输入数据框，不能含空值
    k:聚类类别数目
    start_col:聚类输入数据开始位置（列）
    end_col:聚类输入数据结束位置（列）
    '''
    
    #3.函数内导包
    from sklearn.preprocessing import minmax_scale
    from sklearn.cluster import KMeans
    
    #4.处理过程
    #(1)归一化数据
    df_minmax_scale = minmax_scale(df.loc[:, start_col: end_col], axis=1).round(2)
    #(2)k-means
    kmeans = KMeans(n_clusters=k, random_state=110).fit(df_minmax_scale)    
    df['Labels'] = kmeans.labels_ + 1  # 类标签（从1开始）
    center_df = pd.DataFrame(kmeans.cluster_centers_)
    center_df['Labels'] = list(range(1, k+1))
    
    #5.函数结果 df:聚类结果；center_df:聚类中心
    return df, center_df
########### 测试 ###########
#data_input
'''
name   2018  2019  2020  ...
 A      11    22    33   ...
 B      10    20    30   ... 
 ...    ...   ...   ...  ...
'''
raw_df, center_df = my_kmeans(data_input, 3, '2018', '2020')  
########### 结果 ###########
#raw_df
'''
name   2018  2019  2020  ...   Labels
 A      11    22    33   ...     2
 B      10    20    30   ...     1
 ...    ...   ...   ...  ...     3
'''
#center_df
'''
  0      1      2     ...   Labels
10.5   21.3    32.1   ...     1
11.3   22.1    20.6   ...     2
10.2   18.6    15.4   ...     3
'''