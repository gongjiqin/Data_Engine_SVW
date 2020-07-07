import pandas as pd
import numpy as py
from efficient_apriori import apriori


dataset = pd.read_csv('D:/10_Python/SVW Data Engine/Lesson 4/MarketBasket/Market_Basket_Optimisation.csv', header=None)
print(dataset.shape)

trainsaction = []
for i in range(0, dataset.shape[0]):
    temp = []
    for j in range(0, 20):
        if str(dataset.values[i, j]) != 'nan':
            temp.append(str(dataset.values[i, j]))
    trainsaction.append(temp)

itemsets, rules = apriori(trainsaction, min_support=0.02, min_confidence=0.4)
print('频繁项集：', itemsets)
print('关联规则：', rules)


from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

temp_list = []
for i in range(0,dataset.shape[0]):
    temp_str = ''
    for j in range(0,20):
        if str(dataset.values[i,j]) != 'nan':
        temp_str += str(dataset.values[i,j])+'|'
    temp_list.append(temp_str)
dataset_ml = pd.DataFrame(data=temp_list)
dataset_ml.columns = ['MarketBasket']
dataset_ml.to_csv('temp_data.csv',index=True)

dataset_ml_hot_encoded = dataset_ml.drop('MarketBasket',1).join(dataset_ml.MarketBasket.str.get_dummies('|'))
dataset_ml_hot_encoded = dataset_ml_hot_encoded.dropna(axis=1)
dataset_ml_hot_encoded.to_csv('temp_data.csv',index=True)

itemsets = apriori(dataset_ml_hot_encoded,use_colnames=True, min_support=0.05)
itemsets = itemsets.sort_values(by="support" , ascending=False)
print('-'*20, '频繁项集', '-'*20)
print(itemsets)

rules =  association_rules(itemsets, metric='lift', min_threshold=1)
rules = rules.sort_values(by="lift" , ascending=False)
print('-'*20, '关联规则', '-'*20)
print(rules)