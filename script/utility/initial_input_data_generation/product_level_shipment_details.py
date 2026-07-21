
import pandas as pd
import numpy as np
from script.utility.step_by_step_logging import logging
from script.utility.file_path import new_data_path

product_level_shipment_data = {
        
    "shipment_date" : ['2026-01-03']
    ,"shipment_id" : ['OLR3O0DJS0DFWI']
    ,"product_code" : ['IIDHGKRX8W']
    ,"shipped_quantity" : [90]
    ,"received_quantity" : [90]
    ,"order" : [0]
    ,"removal" : [0]
    ,"current_stock" : [0] 
    ,"difference": [0]

 }

def create_product_level_shipment_details_table() -> pd.DataFrame:
        df = pd.DataFrame(product_level_shipment_data)
        df.to_csv(new_data_path.get('product_level_shipment_details_table'), index=False)
        logging.info("Product level shipment-id details table is created successfully.")
        return df

"""
    "shipment_date" : ['2026-01-01','2026-01-01']
    ,"shipment_id" : ['HFV3O0DJS0JTXRC','RUI950LV03OSYAM']
    ,"product_code" : ['7GDMQCI9KP','RZCVBPAUWU']
    ,"shipped_quantity" : [100,120]
    ,"received_quantity" : [100,120]
    ,"order" : [0,0]
    ,"removal" : [0,0]
    ,"current_stock" : [0,0] 
    ,"difference": [0,0]
"""


"""
    "shipment_date" : ['2026-01-03']
    ,"shipment_id" : ['HFV3O0DJS0JTXRC']
    ,"product_code" : ['4PRTSJVE8WE']
    ,"shipped_quantity" : [150]
    ,"received_quantity" : [150]
    ,"order" : [0]
    ,"removal" : [0]
    ,"current_stock" : [0] 
    ,"difference": [0]
"""