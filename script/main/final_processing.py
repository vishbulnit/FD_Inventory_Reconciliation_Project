
from script.main.order_class import OrderProcessFunctionality
from script.main.removal_class import RemovalProcessFunctionality
from script.main.currentstock_class import CurrentstockProcessFunctionality
from script.main.refer_data_to_process import current_stock_data, order_data, shipment_detail_data, removal_detail_data
from script.main.update_output_final_data import final_output

ocf = OrderProcessFunctionality(order_data)  #  to use order class functionality
rcf = RemovalProcessFunctionality(removal_detail_data) # to use removal class functionality
cscf = CurrentstockProcessFunctionality(current_stock_data)

output_order_final = []
output_removal_final = []


def proces_data():
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
        difference = shipment_detail_data.iat[shp_index,8]


        ### shipment-id mapping on order and output result ###

        order_data_for_process = ocf.filter_and_sort_data(product_code)
        order_data_for_process_index_info = ocf.index_identify(order_data_for_process)
        first_index, last_index, no_of_rows = order_data_for_process_index_info

        if order_data_for_process_index_info[1] is None:
            last_index = 0
        else:
            last_index = order_data_for_process_index_info[1] + 1

        cum_qty = 0
        qty_to_check = received_quantity - (order + removal + current_stock)
        for idx in range(last_index, no_of_rows):   
            qty = order_data_for_process.iat[idx,4]
            cum_qty = cum_qty + qty
            if cum_qty <= qty_to_check:  
                order_data_for_process.iat[idx, 5] = shipment_id
                qty_to_check = qty_to_check - qty
        output_order_final.append(order_data_for_process)
        
        shipment_detail_data.iat[shp_index,5] = order + cum_qty
        #read_write_data.write_data(order_data_for_process,output_data_path.get('order_details_table'))

        ### shipment-id mapping on removal and output result ###

        if qty_to_check > 0: 
            removal_data_for_process = rcf.filter_and_sort_data(product_code)
            removal_data_for_process_index_info = rcf.index_identify(removal_data_for_process)
            first_index, last_index, no_of_rows = removal_data_for_process_index_info   

            if removal_data_for_process_index_info[1] is None:
                last_index = 0
            else:
                last_index = removal_data_for_process_index_info[1] + 1

            rem_cum_qty = 0
            for rem_idx in range(last_index, no_of_rows):   
                rem_qty = removal_data_for_process.iat[rem_idx,3]
                rem_cum_qty = rem_cum_qty + rem_qty
                if rem_cum_qty <= qty_to_check:  
                    removal_data_for_process.iat[rem_idx, 4] = shipment_id
                    qty_to_check = qty_to_check - rem_qty
                    
            output_removal_final.append(removal_data_for_process)

            shipment_detail_data.iat[shp_index,6] = removal + rem_cum_qty
        

        ## check remaining quantity in current stock and update

        if qty_to_check > 0:
            available_stock = cscf.get_available_stock(product_code) 
            if qty_to_check <= available_stock:
                curr_stock = qty_to_check
                shipment_detail_data.iat[shp_index,7] = curr_stock
            else:
                curr_stock = available_stock
            
            shipment_detail_data.iat[shp_index,7] = curr_stock

            diff = received_quantity - (cum_qty + rem_cum_qty + curr_stock)
            shipment_detail_data.iat[shp_index,8] = diff

    final_output().update_order(output_order_final)
    final_output().update_removal(output_removal_final)
    final_output().update_shipmentdetails(shipment_detail_data)

    print(shipment_detail_data)

    # shipment_detail_data.to_csv("data/output_data/product_level_shipment_details_table.csv", index=False)
