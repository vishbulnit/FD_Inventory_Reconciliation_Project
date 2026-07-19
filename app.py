
from script.utility.initial_input_data_generation.product_level_shipment_details import create_product_level_shipment_details_table
from script.utility.initial_input_data_generation.removal_order_details import create_removal_order_details_table
from script.utility.initial_input_data_generation.current_stock_details import create_current_stock_table
from script.utility.initial_input_data_generation.order_details import create_order_details_table

def run_main():
    create_product_level_shipment_details_table()
    create_removal_order_details_table()
    create_current_stock_table()
    create_order_details_table()


if __name__ == '__main__':
    run_main()
    print("Code Executed Successfully.")