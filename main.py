# Sean Perez
# Collab: Dominic Stewart
# Date: 09/11/2022
# Sources: https://pynative.com/python-get-time-difference/#:~:text=To%20get%20the%20difference%20between%20two%2Dtime%2C%20subtract%20time1%20from,time%20to%20the%20microsecond%20resolution.&text=To%20get%20a%20time%20difference%20in%20seconds%2C%20use%20the%20timedelta.

# import numpy as np
import pandas as pd
from datetime import datetime


def loop_dp(filtered_df):
    """Loops through DF and conducts string manipulation to acquire totals for rooms and for organizations"""
    df = filtered_df.reset_index()

    totals_user_id = {}
    totals_room_num = {}
    curr_open = None
    user = None

    for _, row in df.iterrows():

        # To get room_num
        description_list = " ".join(row[5].split(" >")).split(" ")[:4]
        del description_list[1]

        # To get totals
        ##
        timed = row[1].split(" ")
        timed[3] = ''.join(timed[3].split("."))

        # Account for improper formatting of document read by adding zero if missing for the HH
        if timed[2][2] != ":":
            timed[2] = "0"+timed[2]

        # Convert to 24-hour format
        if timed[3] == 'pm':
            if int(timed[2][0:2]) != 12:
                time_24 = str(12 + int(timed[2][0:2]))
                timed[2] = time_24 + timed[2][2:]

        # Remove unnecessary am/pm from list
        timed.pop()
        timed = ' '.join(timed)

        if curr_open is None:
            curr_open = datetime.strptime(timed, '%d/%m/%Y %H:%M:%S')
            user = description_list[1]

        else:
            difference = datetime.strptime(timed, '%d/%m/%Y %H:%M:%S') - curr_open
            # print(difference)
            curr_open = None

            # To get user_ID (skips if there are different users opening and closing
            if user == description_list[1]:
                try:
                    totals_user_id[user] += difference
                except KeyError:
                    totals_user_id[user] = difference

            # To get rooms
            try:
                totals_room_num[description_list[2]] += difference
            except KeyError:
                totals_room_num[description_list[2]] = difference

    # print(totals_user_id)
    # print(totals_room_num)


def main():
    df = pd.read_excel("C:/Users/Sean/Downloads/PatRep260922206883.xls", header=None)
    filtered_df = df[df[5].str.contains('Open|Close') == True]
    filtered_df = filtered_df.dropna(axis=1)

    # string manipulation
    loop_dp(filtered_df)


if __name__ == "__main__":
    main()

