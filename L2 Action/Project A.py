import requests
import pandas as pd
from pandas import DataFrame
from bs4 import BeautifulSoup


def get_page_content(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    html = requests.get(url, headers=headers, timeout=10)
    content = html.text
    soup_f = BeautifulSoup(content, 'html.parser')
    return soup_f

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)


def analysis(soup_object):
    temp = soup_object.find('div', class_='tslb_b')
    df_analysis = pd.DataFrame(columns=['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datetime', 'status'])
    tr_list = temp.find_all('tr')
    for tr in tr_list:
        temp = {}
        td_list = tr.find_all('td')
        if len(td_list) > 0:
            temp['id'] = td_list[0].text
            temp['brand'] = td_list[1].text
            temp['car_model'] = td_list[2].text
            temp['type'] = td_list[3].text
            temp['desc'] = td_list[4].text
            temp['problem'] = td_list[5].text
            temp['datetime'] = td_list[6].text
            temp['status'] = td_list[7].text
            df_analysis = df_analysis.append(temp, ignore_index=True)
    return df_analysis


page_number = 20
base_url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-'
df_result = pd.DataFrame(columns=['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datetime', 'status'])
for i in range(page_number):
    request_url = base_url + str(i+1) + 'shtml'
    soup = get_page_content(request_url)
    df = analysis(soup)
    print(df)
    df_result = df_result.append(df)
df_result.to_excel('result.xlsx', index=False)

