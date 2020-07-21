import pandas as pd
from fbprophet import Prophet


train = pd.read_csv('train.csv')
# print (train.head())

# 转换时间格式
train['Datetime'] = pd.to_datetime(train.Datetime, format='%d-%m-%Y %H:%M')
train.index = train.Datetime
train.drop(['ID', 'Datetime'], axis=1, inplace=True)
# print(train.head())

# 按照天求采样和
daily_train = train.resample('D').sum()
daily_train['ds'] = daily_train.index
daily_train['y'] = daily_train.Count
daily_train.drop(['Count'], axis=1, inplace=True)
print(daily_train.head())

# 预测半年数据
m = Prophet(yearly_seasonality=True, seasonality_prior_scale=0.1)
m.fit(daily_train)
future = m.make_future_dataframe(periods=213)
forecast = m.predict(future)
# print(forecast)
m.plot(forecast)
m.plot_components(forecast)
