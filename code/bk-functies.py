def load_and_group_data(folder, file, headers, sep='|'):
    """
    Loads a CSV file, groups rows by the first column (recordsoort),
    and stores each group as a DataFrame in a dictionary.
    
    Args:
        folder (str): The folder containing the file.
        file (str): The name of the file.
        headers (list): Dictonary containing headers for each recordsoort.
        sep (str): The separator used in the CSV file (default is '|').
        
    Returns:
        dict: A dictionary where keys are the recordsoort from the first column, 
              and values are DataFrames containing the rows for each recordsoort.
    """
    import os
    import pandas as pd

    path = os.path.join(folder, file)

    # Step 2: Open file bekostigingsbestand and make a list of all the unique recordsoorten
    recordsoorten = set()

    with open(path, 'r') as f:
        for line in f:
            row = line.strip().split(sep)
            recordsoorten.add(row[0])  # Add the first column value (recordsoort) to the set

    # Step 3: Initialize a dictionary with the recordsoort as key
    df_dict = {recordsoort: [] for recordsoort in recordsoorten}

    # Step 4: Open the file again and append the row to the appropriate dataframe list
    with open(path, 'r') as f:
        for line in f:
            row = line.strip().split(sep)
            recordsoort = row[0]
            df_dict[recordsoort].append(row)  

    # Step 5: Convert lists to dataframes
    for recordsoort, rows in df_dict.items():
        df_dict[recordsoort] = pd.DataFrame(rows)

    # Step 6: Assign headers from to each dataframe
    for recordsoort, df in df_dict.items():
        if recordsoort in headers:
            columns = headers[recordsoort]
            max_columns = len(columns)
            
            # Adjust the DataFrame to match the expected number of columns
            df = df.iloc[:, :max_columns]  # Limit to expected number of columns
            df.columns = columns
            
            # Add missing columns if any specified columns are absent
            for col in columns:
                if col not in df.columns:
                    df[col] = ''  # Initialize as empty string if missing
        
        # Update the dataframe in the dictionary
        df_dict[recordsoort] = df

    return df_dict
