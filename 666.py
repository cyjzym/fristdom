import  pandas  as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import os
import string
import pymongo
import re
from pymongo import MongoClient

df2=pd.read_excel("F:\pythonSJFX\CYJ python SJXXDM\科发院20190602.xls")["Author Affiliation"]


#定义函数，用[作为分隔符分隔所有字符串
def go_split(s, symbol):
        #拼接正则表达式
        symbol = "[" + symbol + "]+"
        #一次性分隔字符串
        result = re.split(symbol, s)
        #去除空字符
        return [x for x in result if x]
if __name__ == "__main__":
    # 定义初始字符串
    u1 = len(df2)
    #用于存放所有list，防止for循环覆盖结果
    a=[]
    for i in range (u1):
          s = df2[i]
          #定义分隔符
          symbol = '['
          result = go_split(s, symbol)
          a.append(result)
    # print(a)

def make_great(names):
    
    for i in range(len(names)):
       names[i]="[" + names[i]
       print('这是第'+ i + '次运行for')
       #return names
        
b=[]
# for j in range(len(a)):
    #global b=[]
name_list=a[0] 
make_great(name_list)
b.append(name_list)
#     print(name_list)
print(b)