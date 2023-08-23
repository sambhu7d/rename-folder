# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 17:27:16 2023

@author: sambh
"""

import os
import pandas as pd

# Define the path to your CSV file
csv_file_path = 'C:\\Users\\sambh\\Desktop\\name.csv'

# Define the directory where the folders you want to rename are located
folder_directory = 'C:\\Users\\sambh\\Desktop\\count'

# Read the CSV file
df = pd.read_csv(csv_file_path, header=None)

# Create a dictionary mapping from folder names to new names
# Adjust the indices to correctly map folder names to values from A2 to A36
folder_name_mapping = {str(index): name for index, name in df.iloc[1:36, 0].items()}

# Iterate through each folder in the directory
for folder_name, new_name in folder_name_mapping.items():
    old_folder_path = os.path.join(folder_directory, folder_name)
    
    # Only try to rename if the folder actually exists
    if os.path.exists(old_folder_path):
        new_folder_path = os.path.join(folder_directory, new_name)
        os.rename(old_folder_path, new_folder_path)
        print(f'Renamed {old_folder_path} to {new_folder_path}')
