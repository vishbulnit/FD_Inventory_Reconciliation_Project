

import pandas as pd
from typing import Tuple

class CurrentstockProcessFunctionality:

    def __init__(self, order_df: pd.DataFrame):
        self.__curr_stock_df = order_df

    def get_available_stock(self, product_id: str) -> int:
        self.__df = self.__curr_stock_df[self.__curr_stock_df['product_code'] == product_id]
        self.stock_available = self.__df.iloc[0,1]
        return self.stock_available