
import pandas as pd
from typing import List
from script.utility.file_path import output_data_path
from script.utility.read_and_write_file import read_write_data


class final_output(read_write_data):

    def update_order(self, items: List) -> None:
        if len(items) > 0: 
            df = pd.concat([item for item in items])   
            self.write_data(df, output_data_path.get('order_details_table'))
            return None
            
    def update_removal(self, items: List) -> None:
        if len(items) > 0: 
            df = pd.concat([item for item in items])   
            self.write_data(df, output_data_path.get('removal_order_details_table'))
            return None
    
    def update_shipmentdetails(self, df: pd.DataFrame) -> None:
        if len(df) > 0:    
            self.write_data(df, output_data_path.get('product_level_shipment_details_table'))
            return None
    
            