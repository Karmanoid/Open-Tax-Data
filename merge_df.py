#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 11:23:08 2019

@author: karnanoid
"""
import pandas as pd

datafile="./emploee_2017.pkl"
df1=pd.read_pickle(datafile)
print (df1.info())
df1=df1[['inn','num_workers']]
df2=pd.read_pickle("./emploee_2018.pkl")
print (df2.info())
df2=df2[['inn','num_workers']]

#result=pd.concat([df1, df2],ignore_index=True, axis=1, sort=False, keys='inn')

print ('===== JOIN ====')
result=pd.merge (df1, df2, on='inn', how='outer', suffixes=('_2017','_2018'))

print (result.head())
print (result.info())

print ('Всего людей в 2017:', result.num_workers_2017.sum())
print ('Всего людей в 2018:', result.num_workers_2018.sum())

print ('===== АНАЛИЗ  ====')
new=result[result['num_workers_2017'].isnull()]

print ('Новых компаний:','\n')
print (new.info(), new.head())
print ('Новых людей в 2018 году', new.num_workers_2018.sum())

print ('============ one_man_army=============')
one_man_army=new[new['num_workers_2018']==1]
print (one_man_army.num_workers_2018.sum ())

print ('============ man_10=============')
man_10=new[(new['num_workers_2018']>1)&(new['num_workers_2018']<=10)]
print (man_10.num_workers_2018.sum ())


print ('============ man_100=============')
man_100=new[(new['num_workers_2018']>10)&(new['num_workers_2018']<=100)]
print (man_100.num_workers_2018.sum ())

print ('============ man_1000=============')
man_1000=new[(new['num_workers_2018']>100)&(new['num_workers_2018']<=1000)]
print (man_1000.num_workers_2018.sum ())

print ('============ man_10000=============')
man_10000=new[(new['num_workers_2018']>1000)&(new['num_workers_2018']<=10000)]
print (man_10000.num_workers_2018.sum ())

print ('============ >man_10000=============')
man_10000_more=new[new['num_workers_2018']>10001]
print (man_10000_more.num_workers_2018.sum ())
print (man_10000_more.head())


old=result[(result['num_workers_2017'] is not None) & (result['num_workers_2018'].isnull())]

print ('Старых компаний:', '\n')
print (old.info(), old.head())
print ('уволено людей в 2018 году', old.num_workers_2017.sum())


print ('============ one_man_army=============')
one_man_army=old[old['num_workers_2017']==1]
print (one_man_army.num_workers_2017.sum ())

print ('============ man_10=============')
man_10=old[(old['num_workers_2017']>1)&(old['num_workers_2017']<=10)]
print (man_10.num_workers_2017.sum ())
print (man_10.head (10))

print ('============ man_100=============')
man_100=old[(old['num_workers_2017']>10)&(old['num_workers_2017']<=100)]
print (man_100.num_workers_2017.sum ())

print ('============ man_1000=============')
man_1000=old[(old['num_workers_2017']>100)&(old['num_workers_2017']<=1000)]
print (man_1000.num_workers_2017.sum ())

print ('============ man_10000=============')
man_10000=old[(old['num_workers_2017']>1000)&(old['num_workers_2017']<=10000)]
print (man_10000.num_workers_2017.sum ())

print ('============ >man_10000=============')
man_10000_more=old[old['num_workers_2017']>10001]
print (man_10000_more.num_workers_2017.sum ())
print (man_10000_more.head())




print ('===== INTERSECT ====')
intersect=pd.merge (df1, df2, on='inn', how='inner', suffixes=('_2017','_2018'))

print (intersect.head())
print (intersect.info())
print (' людей в 2017 году', intersect.num_workers_2017.sum())
print ('людей в 2018 году', intersect.num_workers_2018.sum())
