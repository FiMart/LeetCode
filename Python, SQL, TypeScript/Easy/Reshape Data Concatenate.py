import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    # Concatenate the two DataFrames along the rows (axis=0)
    concatenated_df = pd.concat([df1, df2], axis=0, ignore_index=True)
    
    # Reset the index of the concatenated DataFrame
    concatenated_df.reset_index(drop=True, inplace=True)
    
    return concatenated_df