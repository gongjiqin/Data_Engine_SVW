from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np


data = pd.read_csv('D:/10_Python/SVW Data Engine/Lesson 3/Mall_Customers.csv')
train_x = data[["Gender", "Age", "Annual Income (k$)", "Spending Score (1-100)"]]
# print(train_x['Gender'])

# 性别转为01
le = LabelEncoder()
train_x['Gender'] = le.fit_transform(train_x['Gender'])
# print(train_x['Gender'])

# 规范化
min_max_scaler = preprocessing.MinMaxScaler()
train_x = min_max_scaler.fit_transform(train_x)
pd.DataFrame(train_x).to_excel('temp.xlsx', index=False)

kmeans = KMeans(n_clusters=3)
kmeans.fit(train_x)
predict_y = kmeans.predict(train_x)
result = pd.concat((data, pd.DataFrame(predict_y)), axis=1)
result.rename({0: u'聚类结果(分组)'}, axis=1, inplace=True)
print(result)
result.to_excel('customer_cluster_result.xlsx', index=False)
