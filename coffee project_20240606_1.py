# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 10:25:16 2024

@author: eva
"""

# --------Coffee shop sample data (11.1.3+)--------
#IBM Cognos Analytics sample data sets
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
# 讀資料
datas = pd.read_csv('201904 sales reciepts.csv')
product = pd.read_csv('product.csv')

#合併資料 data and product品項
result1=pd.merge(datas, product, 
          how='left', on=['product_id'])

#檢查數據 #確認沒有空值 
result1.info()

'''
大家最常買那些品項?
品項的SIZE?
'''

#整理成新的table
temp1 = ['product','product_group','product_category','quantity','unit_price']
result2= result1[temp1]
fliter = (result2["product_category"] == "Coffee")
result2=result2[fliter]
result2['sale'] = result2['quantity'] * result2['unit_price'] 
grouped = result2.groupby('product').sum().reset_index()
grouped = grouped.sort_values(by='quantity', ascending=False) 
print(grouped)
#畫圖
plt.figure(figsize=(30, 8))
bars=plt.bar(grouped['product'],grouped['quantity'])
plt.title('咖啡銷售品項統計')
plt.xlabel('咖啡品項名稱')
plt.ylabel('數量')
plt.ylim(0,1800) #設定y軸顯示範圍
#產生刻度陣列(npArray 類式list)
tick_arr = np.arange(0,1800,200)
plt.xticks(rotation=45) #設定刻度
plt.yticks(tick_arr) #空值代表隱藏刻度


for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, int(yval), va='bottom')

plt.show()