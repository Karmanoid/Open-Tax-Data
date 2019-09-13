#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Этот скрипт конвертирует данные ФНС РФ об уплаченных налогах в формате DataFrame

Скачать сырые данные можно по ссылке https://www.nalog.ru/opendata/7707329152-paytax/

Архив данных за предыдущие года по ссылке ____

Pandas 0.24.1 и выше
"""

import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np
import glob
import re
#если xml-файлы лежат в ином каталоге, укажите корректный путь

files=glob.glob('./taxes/2017/data-20190426-structure-20180110/*.xml')



#print (files)

dataset=[]

for file in files:
    print ('processing...', file)
    
    tree = ET.parse(file)
    root = tree.getroot()
#    print (root.attrib)
    
            
    docs=root.findall('Документ')    
    for i in range (len(docs)):
        item=dict()
#        print (docs[i][0].attrib)
        item['Company']=docs[i][0].attrib.get('НаимОрг')
        item['INN']=docs[i][0].attrib.get('ИННЮЛ')
        taxes=docs[i].findall('СвУплСумНал')
        for tax in taxes:
            item[re.sub(' +', ' ',tax.get('НаимНалог'))]=float(tax.get('СумУплНал'))
        dataset.append (item)

df=pd.DataFrame(dataset)

# добавляем сумму всех уплаченных налогов одной компанией

total=df.sum(axis = 1, skipna = True) 
df['Total']=total

print ('saving dataset...')
##
#сохраняем датасе в текущий каталог
df.to_pickle ('./2017_taxes.pkl')
print (df.info())