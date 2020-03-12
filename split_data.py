""" Split Data Module """

from time import sleep
import numpy as np
import pandas as pd
from utils import pretty_print, get_int_input, clear, get_file, get_file_name

def main_df_split():
    """ Main function to split data files """

    clear()
    pretty_print("You can split the file in equal parts here:", "#")

    try:
        name = get_file()
        pretty_print("How many chunks do you need?", "-")
        number = get_int_input()
        data_frame = pd.read_excel(name)
        split_df = np.array_split(data_frame, number)
        for index, dataframe in enumerate(split_df, 1):
            file_name = get_file_name()
            dataframe.to_excel(f"{file_name}.xlsx", index=False)
            pretty_print(f"File {index} {file_name}.xlsx Saved", "*")

        pretty_print("Have a Nice Day! - @MrunalSalvi", "&")
        sleep(5)

    except FileNotFoundError:
        clear()
        pretty_print("The File Does not Exist.", ":")
        pretty_print("Make Sure your place the file in the working directory.", ":")
        sleep(2)
        main_df_split()

    except Exception as log_error:
        print("Oops something went wrong...")
        print(log_error)
        sleep(10)
