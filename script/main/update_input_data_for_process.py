
import pandas as pd
from script.utility.file_path import new_data_path, input_data_path, output_data_path
from script.utility.read_and_write_file import read_write_data

class input_data_update:

    def update_order(self):

        # updating input data here
        df1 = read_write_data().read_data(output_data_path.get('order_details_table'))
        df2 = read_write_data().read_data(new_data_path.get('order_details_table'))
        combined_df = pd.concat([df1, df2])
        read_write_data().write_data(combined_df,input_data_path.get('order_details_table'))

        # deleting and updating record for new data and output data here
        df2.drop(df2.index, inplace=True)
        read_write_data().write_data(df2,new_data_path.get('order_details_table'))
        df1.drop(df1.index, inplace=True)
        read_write_data().write_data(df1,output_data_path.get('order_details_table'))
        
    def update_shipmentdetail(self):

        # updating input data here
        df1 = read_write_data().read_data(output_data_path.get('product_level_shipment_details_table'))
        df2 = read_write_data().read_data(new_data_path.get('product_level_shipment_details_table'))
        combined_df = pd.concat([df1, df2])
        read_write_data().write_data(combined_df,input_data_path.get('product_level_shipment_details_table'))

        # deleting and updating record for new data and output data here
        df2.drop(df2.index, inplace=True)
        read_write_data().write_data(df2,new_data_path.get('product_level_shipment_details_table'))
        df1.drop(df1.index, inplace=True)
        read_write_data().write_data(df1,output_data_path.get('product_level_shipment_details_table'))

    def update_removal(self):

        # updating input data here
        df1 = read_write_data().read_data(output_data_path.get('removal_order_details_table'))
        df2 = read_write_data().read_data(new_data_path.get('removal_order_details_table'))
        combined_df = pd.concat([df1, df2])
        read_write_data().write_data(combined_df,input_data_path.get('removal_order_details_table'))

        # deleting and updating record for new data and output data here
        df2.drop(df2.index, inplace=True)
        read_write_data().write_data(df2,new_data_path.get('removal_order_details_table'))
        df1.drop(df1.index, inplace=True)
        read_write_data().write_data(df1,output_data_path.get('removal_order_details_table'))

    def update_currentstock(self):
        df1 = read_write_data().read_data(new_data_path.get('current_stock_details_table'))
        read_write_data().write_data(df1,input_data_path.get('current_stock_details_table'))
        read_write_data().write_data(df1,output_data_path.get('current_stock_details_table'))
        df1.drop(df1.index, inplace=True)
        read_write_data().write_data(df1,new_data_path.get('current_stock_details_table'))


input_data_update().update_order()
input_data_update().update_currentstock()
input_data_update().update_removal()
input_data_update().update_shipmentdetail()