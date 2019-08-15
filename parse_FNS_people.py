#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Этот скрипт конвертирует данные ФНС РФ о численности сортрудников компаний в 
единую базу данных в формате DataFrame

Скачать сырые данные можно по ссылке ___

Архив данных за предыдущие года по ссылке ____

Pandas 0.24.1 и выше
"""

import xml.etree.ElementTree as ET
import pandas as pd
import glob

#если xml-файлы лежат в ином каталоге, укажите корректный путь

files=glob.glob('./data-20190801-structure-20180801/*.xml')


print (files)
full_df=pd.DataFrame()
dataset=[]
print ('processing...')
for file in files:
    
    tree = ET.parse(file)
    root = tree.getroot()
    print (len(root))
    item=dict.fromkeys(['Company', 'INN', 'People'])
    for i in range (1,len(root)):
        for child in root[i]:
            try:
                if child.attrib['НаимОрг']:
                    item['Company']=child.attrib['НаимОрг']
                    item['INN']=child.attrib['ИННЮЛ']
            except:
                item['People']=child.attrib['КолРаб']
        dataset.append (item)
        item=dict.fromkeys(['Company', 'INN', 'People'])
df=pd.DataFrame(dataset)

print ('saving dataset...')

#сохраняем датасе в текущий каталог
df.to_pickle ('./2018_people.pkl')
