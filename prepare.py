import pandas as pd
import numpy as np

import acquire

from acquire import new_store_data, get_store_data, get_germany

def prepare_store(): 
    df_store = get_store_data()

    df_store.sale_date = pd.to_datetime(df_store.sale_date)

    df_store = df_store.set_index('sale_date')

    df_store = df_store.sort_index()

    df_store['month'] = df_store.index.month
    df_store['day_of_week'] = df_store.index.day_of_week

    df_store['sales_total'] = df_store['sale_amount'] * df_store['item_price']

    return df_store

def prepare_germany():
    df_germ = get_germany()

    df_germ.Date = pd.to_datetime(df_germ.Date)

    df_germ = df_germ.set_index('Date')

    df_germ = df_germ.sort_index()

    df_germ['month'] = df_germ.index.month
    df_germ['year'] = df_germ.index.year


    mean_value_w=df_germ['Wind'].mean()

    df_germ['Wind'].fillna(value=mean_value_w, inplace=True)

    mean_value_s=df_germ['Solar'].mean()

    df_germ['Solar'].fillna(value=mean_value_s, inplace=True)

    mean_value=df_germ['Wind+Solar'].mean()

    df_germ['Wind+Solar'].fillna(value=mean_value, inplace=True)
