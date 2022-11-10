# Sean Perez
# Collab: Dominic Stewart
# Date: 09/11/2022
# Sources: https://pynative.com/python-get-time-difference/#:~:text=To%20get%20the%20difference%20between%20two%2Dtime%2C%20subtract%20time1%20from,time%20to%20the%20microsecond%20resolution.&text=To%20get%20a%20time%20difference%20in%20seconds%2C%20use%20the%20timedelta.

import numpy as np
import pandas as pd
from datetime import datetime


def loop_dp(filtered_df):
    """Loops through DF and conducts string manipulation to acquire totals for rooms and for organizations"""
    df = filtered_df.reset_index()

    for _, row in df.iterrows():

        # To get room_num
        description_list = " ".join(row[5].split(" >")).split(" ")[:4]
        del description_list[1]
        print(description_list)
        continue
        # To get user_ID

        # To get totals
        ##
        timed = row[1].split(" ")
        timed[3] = ''.join(timed[3].split("."))

        if timed[2][2] != ":":
            timed[2] = "0"+timed[2]

        timed = ' '.join(timed)
        parsed_time = datetime.strptime(timed, '%d/%m/%Y %H:%M:%S %p')
        ##


def main():
    df = pd.read_excel("C:/Users/user/Documents/PatRep260922206883.xls", header=None)
    filtered_df = df[df[5].str.contains('Open|Close') == True]
    filtered_df = filtered_df.dropna(axis=1)

    # string manipulation
    loop_dp(filtered_df)


if __name__ == "__main__":
    main()

