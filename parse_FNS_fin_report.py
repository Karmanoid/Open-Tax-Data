#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Этот скрипт конвертирует данные ФНС РФ из бухгалтерской отчетности (доходы/расходы) в формате DataFrame

Скачать сырые данные можно по ссылке https://www.nalog.ru/opendata/7707329152-revexp/

Архив данных за предыдущие года по ссылке ____

Pandas 0.24.1 и выше
"""

import xml.etree.ElementTree as ET
import pandas as pd

import glob

#если xml-файлы лежат в ином каталоге, укажите корректный путь

files=glob.glob('./fin_reports/2017/data-20190226-structure-20180110/*.xml')



full_df=pd.DataFrame()
dataset=[]
print ('processing...')
for file in files:
    
    tree = ET.parse(file)
    root = tree.getroot()
    for i in range (1,len(root)):
        item=dict()
        for child in root[i]:
            try:
                if child.attrib['НаимОрг']:
                    item['Company']=child.attrib['НаимОрг']
                    item['INN']=child.attrib['ИННЮЛ']
            except:
                item['Revenue']=float(child.attrib['СумДоход'])
                item['Cost']=float (child.attrib['СумРасход'])
        dataset.append (item)


print (dataset[:2])
df=pd.DataFrame(dataset)
df['Profit']=df['Revenue']-df['Cost']
print ('saving dataset...')

#сохраняем датасе в текущий каталог
df.to_pickle ('./2017_fin_rep.pkl')
print (df.info())

