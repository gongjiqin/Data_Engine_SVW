from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import matplotlib.pyplot as plt

city_data = pd.read_csv('D:/10_Python/SVW Data Engine/Lesson 3/car_data.csv', encoding='gbk')
train_x = city_data[['人均GDP', '城镇人口比重', '交通工具消费价格指数', '百户拥有汽车量']]
# print(city_data)
# print(train_x)

# 规范化
min_max_scaler = preprocessing.MinMaxScaler()
train_x = min_max_scaler.fit_transform(train_x)
pd.DataFrame(train_x).to_excel('temp.xlsx', index=False)
# print(train_x)

# 决定组数
sse = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(train_x)
    sse.append(kmeans.inertia_)
x = range(1, 11)
plt.xlabel('K')
plt.ylabel('SSE')
plt.plot(x, sse, 'o-')
plt.show()

# 4组
kmeans2 = KMeans(n_clusters=4)
kmeans2.fit(train_x)
predict_y = kmeans2.predict(train_x)
result = pd.concat((city_data, pd.DataFrame(predict_y)), axis=1)
result.rename({0: u'聚类结果(分组)'}, axis=1, inplace=True)
print(result)
result.to_excel('city_group.xlsx', index=False)
