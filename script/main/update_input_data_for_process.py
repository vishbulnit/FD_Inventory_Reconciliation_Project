
import pandas as pd
import os
from script.utility.file_path import new_data_path

print(os.getcwd())

"""
def update_input_order_data():
    df1 = read_and_write_file.read_data(output_data_path.get('order_details_table'))
    df2 = read_and_write_file.read_data(new_data_path.get('order_details_table'))
    combined_df = pd.concat([df1, df2])
    read_and_write_file.write_data(combined_df,input_data_path.get('order_details_table'))
    #df2.drop(df2.index, inplace=True)
    #write_data(df2,new_data_path.get('order_details_table'))
    return None

def update_input_shipmentdetail_data():
    pass

def update_input_removal_data():
    pass

def update_input_currentstock_data():
    pass
    
"""