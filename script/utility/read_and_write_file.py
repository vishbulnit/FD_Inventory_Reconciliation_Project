
import pandas as pd
from script.utility.step_by_step_logging import logging
from typing import Dict, Any, AnyStr

class read_write_data:

    def write_data(self,df: pd.DataFrame, file_path: str) -> None:
        df.to_csv(file_path, index=False)
        logging.info("Current stock details table is created successfully.")
        return None

    def read_data(self,file_path: str) -> pd.DataFrame:
        df = pd.read_csv(file_path)
        logging.info("Current stock details table is created successfully.")
        return df

