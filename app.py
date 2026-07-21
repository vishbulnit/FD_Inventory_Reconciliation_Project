
from script.utility.initial_input_data_generation import new_data_generation
import script.main.update_input_data_for_process
import script.main.final_processing as fp

def app_run():
    fp.proces_data()


if __name__ == '__main__':
    app_run()
    print("Program executed successfully.")
