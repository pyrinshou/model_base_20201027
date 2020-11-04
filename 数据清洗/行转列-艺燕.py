def trans(df,num,key,value):
	# 1.函数功能说明
	# 对df的指定列进行转置
	
	# 2.参数说明
	''' 
	:param df: 传入一个DataFrame格式的数据集
	:param num: 传入需要开始转置的列序号,从1开始算
	:param key: 对列名称的命名
	:param value: 对值那一列的命名
	:return: 返回一个新的DataFrame 
	''' 
	
	# 3.函数内部导包 
	import pandas as pd
	
	# 4.处理过程 
  list_name = list(df)
  df_new = df.set_index(list_name[0:num-1],drop=True)
  df_new = df_new.stack(dropna=False)
  df_new = df_new.reset_index()
  df_new = df_new.rename(columns={'level_2': key, 0: value})
	
	# 5.结果
  return df_new


# 测试
# table2
'''
    日期                   商圈名称             18:00:00          19:00:00        20:00:00
    2020-07-01  00:00:0    中山路商圈夜市       9278.55           9243.65         9040.6
    2020-07-01  00:00:00   下杭历史文化名街     2.663125          3.73145         1.911675	
'''
df = table2
num = 3
key = '时间'
value = '用电量'
table3 = trans(table2, 3, '时间', '用电量')

# table3结果为
'''
日期         商圈名称              时间         用电量
2020-07-01   中山路商圈夜市        18:00:00     9278.55
2020-07-01   中山路商圈夜市        19:00:00     9243.65
2020-07-01   中山路商圈夜市        20:00:00     9040.60
2020-07-01   上下杭历史文化名街    18:00:00     2.66
2020-07-01   上下杭历史文化名街    19:00:00     3.73
2020-07-01   上下杭历史文化名街    0:00:00      1.91
'''
