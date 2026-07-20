
import pandas as pd
import numpy as np
from step_by_step_logging import logging
from file_path import new_data_path, input_data_path, output_data_path

def write_data(df: pd.DataFrame, file_path: str) -> None:
    df.to_csv(file_path, index=False)
    logging.info("Current stock details table is created successfully.")
    return None


def read_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    logging.info("Current stock details table is created successfully.")
    return df


if __name__ == "__main__":
  
    new_df = []
    for item, value in new_data_path.items():
        new_df.append(read_data(value))

    i = 0
    for item, value in input_data_path.items():
        write_data(new_df[i], value)
        i += 1

    j = 0
    for item, value in output_data_path.items():
        write_data(new_df[j], value)
        j += 1    
    
    """
    df = read_data(new_data_path.get('current_stock_details_table'))
    write_data(df, input_data_path.get('current_stock_details_table'))

    df = read_data(new_data_path.get('order_details_table'))
    write_data(df, output_data_path.get('order_details_table'))
    """