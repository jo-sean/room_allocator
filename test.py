import pandas as pd

def main():
    #Create a dictionary of dataframes with the sheet as the key
    df_dict = pd.read_excel("C:/Users/user/Documents/RoomAllocation/PatRep260922206883.xls", sheet_name=None, header=None)
    
    #Concatenate dataframes in dictionary into a single dataframe
    df = pd.concat(df_dict)

    #Keep only rows containing strings "Open" or "Close" and columns that are not NaN
    filtered_df = df[df[5].str.contains('Open|Close') == True]
    filtered_df = filtered_df.dropna(axis=1)

    filtered_df.to_csv("test.csv", index=False, header=None)

if __name__ == "__main__":
    main()