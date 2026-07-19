
import pandas as pd
import numpy as np
from script.utility.step_by_step_logging import logging

product_level_shipment_data = {
    "shipment_date" : ['2026-01-01','2026-01-01']
    ,"shipment_id" : ['HFV3O0DJS0JTXRC','RUI950LV03OSYAM']
    ,"product_code" : ['7GDMQCI9KP','RZCVBPAUWU']
    ,"shipped_quantity" : [100,120]
    ,"received_quantity" : [100,120]
    ,"order" : [0,0]
    ,"removal" : [0,0]
    ,"current_stock" : [0,0] 
}

def create_product_level_shipment_details_table() -> pd.DataFrame:
    df = pd.DataFrame(product_level_shipment_data)
    df.to_csv("data/input_data/product_level_shipment_details_table.csv", index=False)
    logging.info("Product level shipment-id details table is created successfully.")
    return df

