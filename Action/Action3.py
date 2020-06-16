import pandas as pd
from pandas import DataFrame

result = pd.read_csv('D:/10_Python/SVW Data Engine/Lesson 1/Data_Engine_with_Python-master/L1/car_data_analyze/car_complain.csv')
result = result.drop('problem', 1).join(result.problem.str.get_dummies(','))
# print(result)
df_brand = result.groupby(['brand'])['id'].agg(['count']).sort_values('count', ascending=False)
print('品牌投诉总数\n', df_brand)
df_car_model = result.groupby(['car_model'])['id'].agg(['count']).sort_values('count', ascending=False)
print('车型投诉总数\n', df_car_model)
df_avg = result.groupby(['brand', 'car_model'])['id'].agg(['count']).groupby(['brand']).mean().\
    sort_values('count', ascending=False)
print('平均品牌车型投诉总数\n', df_avg)
