
import pandas as pd
import numpy as np
import random
from script.utility.step_by_step_logging import logging
from script.utility.file_path import new_data_path


random_date = ['2026-01-11','2026-01-12','2026-01-10','2026-01-08','2026-01-09','2026-01-13','2026-01-14','2026-01-07','2026-01-06']

order_data = {

    "order_date" : random.choices(random_date, k = 10)
    ,"order_id" : random.sample(range(1000000,5000000), 10)
    ,"product_code" : random.choices(['7GDMQCI9KP','RZCVBPAUWU'], k = 10)
    ,"sale" : random.sample(range(1,500), 10)
    ,"quantity" : random.choices([1,2], k = 10)
    ,"shipment_id_mapped" : [np.nan for _ in range(1,11)]

}

def create_order_details_table() -> pd.DataFrame:
    df = pd.DataFrame(order_data)
    df.to_csv(new_data_path.get('order_details_table'), index= False)
    logging.info("Order details table is created successfully.")
    return df

"""
    "order_date" : random.choices(random_date, k = 5)
    ,"order_id" : [1000 + r for r in range(11,16)]
    ,"product_code" : random.choices(['7GDMQCI9KP','RZCVBPAUWU'], k = 5)
    ,"sale" : random.sample(range(1,500), 5)
    ,"quantity" : random.choices([1,2], k = 5)
    ,"shipment_id_mapped" : [np.nan for _ in range(11,16)]
"""    


"""
    "order_date" : random.choices(random_date, k = 10)
    ,"order_id" : [1000 + r for r in range(1,11)]
    ,"product_code" : random.choices(['7GDMQCI9KP','RZCVBPAUWU'], k = 10)
    ,"sale" : random.sample(range(1,500), 10)
    ,"quantity" : random.choices([1,2], k = 10)
    ,"shipment_id_mapped" : [np.nan for _ in range(1,11)]
"""