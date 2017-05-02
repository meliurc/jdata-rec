# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
from sklearn import preprocessing

s = ['0.0', '11.0', '12.0', '13.0', '14.0', '15.0', '16.0', '17.0', '18.0', '19.0', '21.0', '22.0', '23.0', '24.0',
     '25.0', '26.0', '27.0', '28.0', '29.0', '31.0', '32.0', '33.0', '34.0', '36.0', '39.0', '110.0', '111.0', '112.0',
     '113.0', '114.0', '115.0', '116.0', '119.0', '120.0', '121.0', '122.0', '124.0', '125.0', '210.0', '211.0',
     '216.0', '217.0', '218.0', '219.0', '220.0', '221.0', '222.0', '223.0', '224.0', '311.0', '312.0', '313.0',
     '315.0', '316.0', '318.0', '319.0', '320.0', '321.0', '322.0', '323.0', '325.0', '326.0', '328.0', '329.0',
     '331.0', '333.0', '334.0', '335.0', '336.0', '337.0', '339.0', '340.0', '341.0', '342.0', '343.0', '344.0',
     '345.0', '346.0', '347.0', '348.0', '999']

def add_features(group):
    group['type_1'] = sum(group['type'] == 1)
    group['type_2'] = sum(group['type'] == 2)
    group['type_3'] = sum(group['type'] == 3)
    group['type_3'] = sum(group['type'] == 3)
    group['type_4'] = sum(group['type'] == 4)
    group['type_5'] = sum(group['type'] == 5)
    group['type_6'] = sum(group['type'] == 6)

    oneHotKeyModel = pd.get_dummies(group['model_id'])
    oneHotKeyModel.columns = ['model_id_' + str(int(x)) for x in oneHotKeyModel.columns]

    group = group.join(oneHotKeyModel)

    return group

actionDf2 = pd.read_csv('../data/JData_Action_201602.csv', dtype={'user_id': int, 'sku_id': int, 'time': str,
                                                                  'type': int, 'cate': int, 'brand': int},
                                                           nrows=2)
actionDf2 = actionDf2.drop_duplicates()
actionDf2['model_id'] = actionDf2['model_id'].fillna(999).astype(int)
# oneHotKeyModel = pd.get_dummies(actionDf2['model_id'])
# oneHotKeyModel.columns = ['model_id_' + str(int(x)) for x in oneHotKeyModel.columns]
# actionDf2 = actionDf2.join(oneHotKeyModel)
# actionDf2['type_1'] = sum(actionDf2['type'] == 1)
print actionDf2

temp_df = actionDf2.groupby(['user_id', 'sku_id']).apply(add_features)
print temp_df

"[0.0 11.0 12.0 13.0 14.0 15.0 16.0 17.0 18.0 19.0 21.0 22.0 23.0 24.0 25.0\
 26.0 27.0 28.0 29.0 31.0 32.0 33.0 34.0 36.0 39.0 110.0 111.0 112.0 113.0\
 114.0 115.0 116.0 119.0 120.0 121.0 122.0 124.0 125.0 210.0 211.0 216.0\
 217.0 218.0 219.0 220.0 221.0 222.0 223.0 224.0 311.0 312.0 313.0 315.0\
 316.0 318.0 319.0 320.0 321.0 322.0 323.0 325.0 326.0 328.0 329.0 331.0\
 333.0 334.0 335.0 336.0 337.0 339.0 340.0 341.0 342.0 343.0 344.0 345.0\
 346.0 347.0 348.0 'nan']".split(' ')
