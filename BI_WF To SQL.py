
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import pymssql
import cx_Oracle
from sqlalchemy import create_engine

engine=create_engine('mssql+pymssql://sa:Abcd12345@10.1.93.200/wanda')
Report_date=input('Please input Report Date(yyyymmdd):')
wf_version=input('Please input Weekly Forecast Version with Fst170601:')

#==============================================================================
# Oracle数据库连接
#==============================================================================
username='WANDASEMP2'
pwd='wanda_2016'
IP='10.199.134.27:1521/htbi'
db1=cx_Oracle.connect(username,pwd,IP)
cursor = db1.cursor()

sql = "select Resort_code,report_date,Business_Month,Indicator_Name,Indicator_Desc,Forecast_Value_M,Budget_STR_Value_M,Budget_ORG_Value_M,Lasty_Value_M from WANDASEMP2.V_MODEL_HOTEL_FORECAST_D where report_date ='"+Report_date+"'"
cursor.execute(sql)

result = cursor.fetchall()
fields=cursor.description
column=[]

for field in range(0,len(fields)):
    column.append(fields[field][0])

data1=pd.DataFrame(result,columns=column)
data1.fillna(0,inplace=True)
data1['DATA_DATE_Year']=data1['BUSINESS_MONTH'].str[:4]
data1['DATA_DATE_Month']=data1['BUSINESS_MONTH'].str[4:]

#==============================================================================
# SQL Server数据库连接
#==============================================================================
ip='4BQGENW6GCHWI6V'
user='sa'
pwd='Ppguiandzp543'
con=pymssql.connect(ip,user,pwd,'mytest')
map_small=pd.read_sql('select Small_Code, BI_Mapping,BI_Mapping_Type from WFCode ',con)

data2=pd.merge(data1,map_small,left_on='INDICATOR_NAME',right_on='BI_Mapping',how='left')

data2.drop(['REPORT_DATE','BUSINESS_MONTH','INDICATOR_NAME','INDICATOR_DESC','BUDGET_STR_VALUE_M','BUDGET_ORG_VALUE_M','LASTY_VALUE_M','BI_Mapping'],axis=1,inplace=True)

data2=data2.rename(columns={'RESORT_CODE':'Hotel_Code','FORECAST_VALUE_M':'Date1'})
data2['Version']=wf_version

data3=data2.groupby(['Hotel_Code','DATA_DATE_Year','DATA_DATE_Month','BI_Mapping_Type']).sum()

data4=data3.query('BI_Mapping_Type==["REV"]').stack()

data5=data4.reset_index()
data5.drop(['level_4'],axis=1,inplace=True)
data5=data5.rename(columns={0:'Date1'})
data5['Small_Code']='999999'

data5['Version']=wf_version

data6=data2.append(data5)

data6.drop(['BI_Mapping_Type'],axis=1,inplace=True)

data6.head()

data6.to_sql('WF2017A',engine,if_exists='append',index=False,chunksize=10000)

input('<enter>')
