# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd

actionDf2 = pd.read_csv('../data/JData_Action_201602.csv', dtype={'user_id': int, 'sku_id': int, 'time': str,
                                                                  'type': int, 'cate': int, 'brand': int})
actionDf2 = actionDf2.drop_duplicates()
productDf = pd.read_csv('../data/JData_Product.csv', dtype={'sku_id': int, 'a1': int, 'a2': int, 'a3': int,
                                                            'cate': int, 'brand': int})
userDf = pd.read_csv('../data/JData_User.csv', dtype={'user_id': int, 'user_lv_cd': int, 'usre_reg_tm': str})
userDf['age'].fillna('-1', inplace=True)
userDf['sex'].fillna(2, inplace=True)


time_mask1 = (actionDf2['time'] > '2016-02-01') \
             & (actionDf2['time'] < '2016-02-08')
actionDf2_week1 = actionDf2[time_mask1]
group = actionDf2_week1.groupby('user_id')

time_mask2 = (actionDf2['time'] > '2016-02-08') \
             & (actionDf2['time'] < '2016-02-13')
actionDf2_week2 = actionDf2[['user_id', 'sku_id', 'type']][time_mask2]
type_mask = (actionDf2_week2['type'] != 4)
actionDf2_week2['type'][type_mask] = 0
actionDf2_week2['type'][~type_mask] = 1

commentDf = pd.read_csv('../data/JData_Comment.csv')