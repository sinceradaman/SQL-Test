# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

#===================生成DataFrame==============================================
# data=DataFrame(np.arange(16).reshape((4,4)),
#                index=['Ohio','Colorado','Utah','New York'],
#                columns=['one','two','three','four'])
# data
#==============================================================================

#=======================函数===================================================
#  def say(a=1,b=1):
#    print a,b
#  return;
#  def haha(**kw):
#    apply(say,(),kw)；：
#    print haha(a='a',b='b')
#  return;
#=========================Merge================================================
#
#df1=DataFrame({'key':['b','b','a','c','a','a','b'],
#               'data1':range(7)})
#df2=DataFrame({'key':['a','b','c'],
#               'data2':range(3)})
#
#    pd.merge(df1,df2,on='key',how='outer')
#=========================Groupby================================================
#df=DataFrame({'key1':['a','a','b','b','a'],
#              'key2':['one','two','one','two','one'],
#              'data1':np.random.randn(5),
#              'data2':np.random.randn(5)})
#grouped=df['data1'].groupby(df['key1'])
#grouped.mean()
#
#pieces=dict(list(df.groupby(['key1','key2'])))
#pieces['a','one']
#=========================Load csv==============================================
tips=pd.read_csv('C:/Users/Administrator/Desktop/Python_SQL Test/tips.csv')    
tips['tip_pct']=tips['tip']/tips['total_bill']
grouped=tips.groupby(['sex','smoker'])

tips[(tips['sex']==u'Male')&(tips['smoker']==u'No')]
tips.loc[:10][(tips['sex']==u'Male')&(tips['smoker']==u'No')]
