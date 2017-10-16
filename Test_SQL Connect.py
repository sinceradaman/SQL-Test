#encoding=utf-8
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
from sqlalchemy import create_engine
import cx_Oracle
import sys
#import os

#===================Create the Chinese STR Environment ==================
#reload(sys)  
sys.setdefaultencoding('utf8')  
#os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
 
#===================Oracle Connnect======================================
#username='WANDASEMP2'
#pwd='wanda_2016'
#IP='10.199.134.27:1521'
#
'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine("oracle+cx_oracle://wdhotel_birm:ng1hAA8fiLOxIddS@htbi")

sql="SELECT * FROM WANDASEMP2.V_MODEL_HOTEL_ANALYSIS_D WHERE ROWNUM<=10"

with engine.connect() as conn, conn.begin():
    data = pd.read_sql(sql, conn)
    
#text = data.loc[:,'dow']
#text = pd.Series([text[item].decode("utf8").encode("utf8") for item in text])
#data.loc[:,'dow'] = text
    
#cx_Oracle.connect('username', 'pwd', 'IP/htbi') 
  
#===================get SQLData to DataFrame ============================
'经测试不能用赋值的方式读取，系统报未知错误，改成双引号""即可'
#username='sa'
#pwd='Ppguiandzp543'
#IP='4BQGENW6GCHWI6V'
#engine = create_engine('mssql+pymssql://username:pwd@IP/mytest')
#
#'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
#engine = create_engine('mssql+pymssql://sa:Ppguiandzp543'
#                       '@4BQGENW6GCHWI6V/mytest')
#with engine.connect() as conn, conn.begin():
#    data = pd.read_sql('2018 Budget_raw data', conn)
    
#===================SQL Server Connnect===================================== 
#import pymssql
#
#conn=pymssql.connect(host='4BQGENW6GCHWI6V',user='sa',password='Ppguiandzp543',
#                     database='mytest')
#cur=conn.cursor()
#cur.execute('select top 5 * from fruits')
#Fruits=cur.fetchall()
#
#cur.close()
#conn.close()



