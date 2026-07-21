
import pandas as pd
import numpy as np
from script.utility.step_by_step_logging import logging
from script.utility.file_path import new_data_path

current_stock_details = {

    "product_code" : ['7GDMQCI9KP','RZCVBPAUWU','4PRTSJVE8WE']
    ,"stock_available" : [100,120,150]

}

def create_current_stock_table() -> pd.DataFrame:
    df = pd.DataFrame(current_stock_details)
    df.to_csv(new_data_path.get('current_stock_details_table'), index=False)
    logging.info("Current stock details table is created successfully.")
    return df
