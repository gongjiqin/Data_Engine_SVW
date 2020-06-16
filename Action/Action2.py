import pandas as pd
from pandas import DataFrame

df = DataFrame(data={'语文': [68, 95, 98, 90, 80], '数学': [65, 76, 86, 88, 90], '英语': [30, 98, 88, 77, 90]},
               index=['张飞', '关羽', '刘备', '典韦', '许诸'], columns=['语文', '数学', '英语'])
# print(df.describe())
print(df)
print('平均成绩：', '\n', df.mean())
print('最小成绩', '\n', df.min())
print('最大成绩', '\n', df.max())
print('方差', '\n', df.var())
print('标准差', '\n', df.std())
df['总分'] = df.sum(axis=1)
print(df.sort_values(by='总分', ascending=True))