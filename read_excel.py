import pandas as pd
import os
from get_file import get_file_name
from total_sums import loop_dp


def read_excel_file():
    """Opens Excel file and extracts contents into dataframe,
    returns two csv files with the totals for users and for rooms"""

    file_name = get_file_name()
    df = pd.read_excel(file_name, sheet_name=None, header=None)

    # Retrieves only the file name from the path
    file_name = os.path.splitext(os.path.basename(file_name))[0]

    # Concatenate dataframes in dictionary into a single dataframe
    df = pd.concat(df)

    filtered_df = df[df[5].str.contains('Open|Close') == True]
    filtered_df = filtered_df.dropna(axis=1)

    # string manipulation
    totals_user_id, totals_room_num = loop_dp(filtered_df)

    # Source: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_dict.html
    # Convert to dataframes
    df1 = pd.DataFrame.from_dict(totals_user_id, orient="index")
    df2 = pd.DataFrame.from_dict(totals_room_num, orient="index")

    # Source: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
    # Source: https://pandas.pydata.org/pandas-docs/version/0.7.0/generated/pandas.DataFrame.to_csv.html
    df1.to_csv(f'totals_per_user_{file_name}.csv', index_label=['User ID'], header=['Total Time Used'])
    df2.to_csv(f'totals_per_room_{file_name}.csv', index_label=['Room Number'], header=['Total Time Used'])
