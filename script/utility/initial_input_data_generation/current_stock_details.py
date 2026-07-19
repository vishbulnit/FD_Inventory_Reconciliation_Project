
import pandas as pd
import numpy as np
from script.utility.step_by_step_logging import logging

current_stock_details = {
    "product_code" : ['7GDMQCI9KP','RZCVBPAUWU']
    ,"stock_available" : [100,120]
}

def create_current_stock_table() -> pd.DataFrame:
    df = pd.DataFrame(current_stock_details)
    df.to_csv("data/input_data/current_stock_details_table.csv", index=False)
    logging.info("Current stock details table is created successfully.")
    return df

