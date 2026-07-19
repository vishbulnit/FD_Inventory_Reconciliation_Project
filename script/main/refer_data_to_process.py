

import pandas as pd
from typing import Dict

dict_data = {
"shipment_detail_path" : 'data/input_data/product_level_shipment_details_table.csv'
,"removal_detail_path" : 'data/input_data/removal_order_details_table.csv'
,"current_stock_path" : 'data/input_data/current_stock_details_table.csv'
,"order_path" : 'data/input_data/order_details_table.csv'
}

def list_of_data_required_for_processing(items: Dict) -> Dict:
    data_list = dict()
    for item in items:
        data_list[item] = pd.read_csv(dict_data[item])
    return data_list

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