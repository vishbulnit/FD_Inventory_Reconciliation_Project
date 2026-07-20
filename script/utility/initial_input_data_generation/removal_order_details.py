
import pandas as pd
import numpy as np
from script.utility.step_by_step_logging import logging
from script.utility.file_path import new_data_path

removal_details = {
    "removal_date" : ['2026-01-04','2026-01-05','2026-01-06']
    ,"removal_id" : ['rm1','rm2','rm3']
    ,"product_code" : ['7GDMQCI9KP','RZCVBPAUWU','RZCVBPAUWU']
    ,"removal_quantity" : [2,1,1]
}

def create_removal_order_details_table() -> pd.DataFrame:
    df = pd.DataFrame(removal_details)
    df.to_csv(new_data_path.get('removal_order_details_table'), index=False)
    logging.info("Removal order details table is created successfully.")
    return df

