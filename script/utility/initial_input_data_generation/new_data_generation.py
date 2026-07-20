
from script.utility.initial_input_data_generation.product_level_shipment_details import create_product_level_shipment_details_table
from script.utility.initial_input_data_generation.removal_order_details import create_removal_order_details_table
from script.utility.initial_input_data_generation.current_stock_details import create_current_stock_table
from script.utility.initial_input_data_generation.order_details import create_order_details_table
from script.utility.file_path import new_data_path, input_data_path, output_data_path
from script.utility.read_and_write_file import read_write_data

class new_data_movement:

    def update_new(self) -> None:
        
        create_product_level_shipment_details_table()
        create_removal_order_details_table()
        create_current_stock_table()
        create_order_details_table()
        
        return None

    def update_input_output(self) -> None:
        
        new_df = []
        for item, value in new_data_path.items():
            new_df.append(read_write_data().read_data(value))

        i = 0
        for item, value in input_data_path.items():
            read_write_data().write_data(new_df[i], value)
            i += 1

        j = 0
        for item, value in output_data_path.items():
            read_write_data().write_data(new_df[j], value)
            j += 1    
        
        return None

ndm = new_data_movement()
ndm.update_new()
ndm.update_input_output()

"""
df = read_data(new_data_path.get('current_stock_details_table'))
write_data(df, input_data_path.get('current_stock_details_table'))

df = read_data(new_data_path.get('order_details_table'))
write_data(df, output_data_path.get('order_details_table'))
"""    



