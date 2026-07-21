

import pandas as pd
from typing import Tuple

class RemovalProcessFunctionality:

    def __init__(self, order_df: pd.DataFrame):
        self.__removal_df = order_df

    def filter_and_sort_data(self, product_id: str) -> pd.DataFrame:
        self.__df = self.__removal_df[self.__removal_df['product_code'] == product_id]
        self.__df = self.__df.sort_values(by=['removal_date']).reset_index(drop=True)
        return self.__df
    
    def index_identify(self, df: pd.DataFrame) -> Tuple:
        self.first_index = df['shipment_id_mapped'].first_valid_index()
        self.last_index = df['shipment_id_mapped'].last_valid_index()
        self.no_of_rows = len(df)
        return self.first_index, self.last_index, self.no_of_rows
