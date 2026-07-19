
import pandas as pd
import numpy as np
import random
from script.utility.step_by_step_logging import logging


random_date = ['2026-01-11','2026-01-12','2026-01-10','2026-01-08','2026-01-09','2026-01-13','2026-01-14','2026-01-07','2026-01-06']

order_data = {

    "order_date" : random.choices(random_date, k = 50)
    ,"order_id" : [1000 + r for r in range(1,51)]
    ,"product_code" : random.choices(['7GDMQCI9KP','RZCVBPAUWU'], k = 50)
    ,"sale" : random.sample(range(1,500), 50)
    ,"quantity" : random.choices([1,2,3,4,5], k = 50)
    ,"shipment_id_mapped" : [np.nan for _ in range(1,51)]
    
}

def create_order_details_table() -> pd.DataFrame:
    df = pd.DataFrame(order_data)
    df.to_csv("data/input_data/order_details_table.csv", index= False)
    logging.info("Order details table is created successfully.")
    return df

