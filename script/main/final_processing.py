

from refer_data_to_process import list_of_data_required_for_processing, dict_data
from order_class import OrderProcessFunctionality


# All 4 datapoints are made available
data_list = list_of_data_required_for_processing(dict_data) 
shipment_detail_data, removal_detail_data, current_stock_data, order_data = data_list.values()

"""
print(shipment_detail_data.head(2))
print(removal_detail_data.head(2))
print(current_stock_data.head(2))
print(order_data.head(2))

"""

# Order functionality added
o = OrderProcessFunctionality(order_data)


# shipment-id processing
for shp_index, shp_row in shipment_detail_data.iterrows():

    shipment_date = shipment_detail_data.iat[shp_index,0]
    shipment_id = shipment_detail_data.iat[shp_index,1]
    product_code = shipment_detail_data.iat[shp_index,2]
    shipped_quantity = shipment_detail_data.iat[shp_index,3]
    received_quantity = shipment_detail_data.iat[shp_index,4]
    order = shipment_detail_data.iat[shp_index,5]
    removal = shipment_detail_data.iat[shp_index,6]
    current_stock = shipment_detail_data.iat[shp_index,7]

    order_data_for_process = o.filter_and_sort_data(product_code)
    order_data_for_process_index_info = o.last_row_identify(order_data_for_process)

    if order_data_for_process_index_info[1] is None:
        idx = 0
    else:
        idx = order_data_for_process_index_info[1] + 1

    quantity_updated = 0
    for index, row in order_data_for_process.iterrows():   
         quantity_updated = quantity_updated + order_data_for_process.iat[index,4]
         order_data_for_process.iat[index, 5] = shipment_id
    
    shipment_detail_data.iat[shp_index,5] = quantity_updated

shipment_detail_data.to_csv("data/output_data/product_level_shipment_details_table.csv", index=False)
