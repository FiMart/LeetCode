import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    # Drop duplicate rows based on the 'email' column
    customers = customers.drop_duplicates(subset='email')
    
    # Return the modified DataFrame
    return customers