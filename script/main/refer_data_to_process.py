

import pandas as pd
from typing import Dict
from script.utility.file_path import input_data_path
from script.utility.read_and_write_file import read_write_data


def load_input_data(items: Dict) -> Dict:
    data_list = dict()
    for item in items:
        data_list[item] = read_write_data().read_data(items.get(item))
    return data_list

lid = load_input_data(input_data_path)
current_stock_data, order_data,  shipment_detail_data, removal_detail_data  = lid.values()

"""
data_list = list_of_data_required_for_processing(dict_data) 

for item in data_list:
    print(item, type(data_list[item]))
    print(data_list[item].head(5))
"""
"""
def product_shipment_detail_data(shipment_detail_path) -> pd.DataFrame:
    df = pd.read_csv(shipment_detail_path)
    return df

def removal_data(removal_detail_path) -> pd.DataFrame:
    df = pd.read_csv(removal_detail_path)
    return df

def current_stock_data(current_stock_path) -> pd.DataFrame:
    df = pd.read_csv(current_stock_path)
    return df

def order_data(order_path) -> pd.DataFrame:
    df = pd.read_csv(order_path)
    return df
"""