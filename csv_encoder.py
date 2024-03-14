import csv
import os
import pandas as pd
import magic




# Usage example
current_folder = os.path.dirname(os.path.abspath(__file__))
csvs_folder = os.path.join(current_folder, 'superset_data/debts')

df_list = []
for file in os.listdir(csvs_folder):
    file_name = file.split('.')[0]
    input_file = os.path.join(csvs_folder, file)
    
    encoding = magic.Magic(mime_encoding=True,).from_file(input_file)
    df = pd.read_csv(input_file, encoding=encoding)
    # Remove indicator name
    df_long = pd.melt(df, id_vars=['country_name', 'indicator_name'], var_name='year', value_name=file_name)
    df_long['year'] = pd.to_numeric(df_long['year'])
    # df_pivot = df_long.pivot_table(index=['country_name', 'year'], columns='indicator_name', values=file_name).reset_index()
    # df_pivot = df_pivot.rename_axis(None, axis=1)  # Remove the axis name if any
    # df_pivot.reset_index(inplace=True)

    df_list.append(df_long)

df = pd.concat(df_list, axis=0)
df.to_csv('debts.csv', index=False)



