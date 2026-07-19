
import pandas as pd
from typing import Tuple

class OrderProcessFunctionality:

    def __init__(self, order_df: pd.DataFrame):
        self.order_df = order_df

        #self.order_path = 'data/input_data/order_details_table.csv'
        #self.order_df = pd.read_csv(self.order_path)
        #print(self.order_df.head(1))

    def filter_and_sort_data(self, product_id: str) -> pd.DataFrame:
        self.df = self.order_df[self.order_df['product_code'] == product_id]
        self.df = self.df.sort_values(by=['order_date']).reset_index(drop=True)
        #print(len(self.df))
        return self.df
    
    def last_row_identify(self, df: pd.DataFrame) -> Tuple:
        self.last_index = df['shipment_id_mapped'].last_valid_index()
        self.first_index = df['shipment_id_mapped'].first_valid_index()
        return self.first_index, self.last_index


# used for data validation
if __name__ == "__main__":
    order_path = 'data/input_data/order_details_table.csv'
    order_df = pd.read_csv(order_path)
    o = OrderProcessFunctionality(order_df)
    df1 = o.filter_and_sort_data('7GDMQCI9KP')
    print(df1)
    index_num = o.last_row_identify(df1)
    print(index_num)
    







