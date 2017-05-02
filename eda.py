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

actionDf2.groupby('sku_id').count().describe()
temp_df = actionDf2.groupby('sku_id').count()
print np.percentile(temp_df['user_id'] ,95)  #  \\ output: 2216.8

actionDf2.groupby('user_id').count().describe()
temp_df = actionDf2.groupby('user_id').count()
print np.percentile(temp_df['sku_id'] ,95)   #  \\ output: 610
print np.percentile(temp_df['sku_id'] ,95)   #  \\ output: 1340

hot_users = temp_df.index[temp_df['sku_id'] > 1340]
print np.unique(actionDf2['type'][actionDf2['user_id'] == hot_users[0]])

actionDf2[actionDf2['cate'] == 8].groupby('user_id').count().describe()
