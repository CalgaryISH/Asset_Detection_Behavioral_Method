# -----------------------------------------------------------------------------
# File Name: main.py
# Version: 0.1
# Author: Subroto Kumer Deb Nath
# Email: subroto.ece.ku@gmail.com
# Description: Detects control, status, configuration, data, and parameter signals
#              from individual Verilog/SystemVerilog file and logs them into a CSV file.
#
# Copyright (c) 2025 Subroto Kumer Deb Nath
# This file is part of an open-source project and is released under the MIT License.
# You are free to use, modify, and distribute this file with proper attribution.
# -----------------------------------------------------------------------------

import os
import re
import csv
from pathlib import Path

from rules.control_sig import *
from rules.status_sig import *
from rules.configuration_sig import *
from rules.data_sig import *
from rules.para_sig import *


asset_dataset = []


path = input(r"Enter the IP/File Directory Here: ")


def asset_detector_individual_file(directory):
    total_asset_in_path = []
    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith(".sv") or file_name.endswith(".v"): #To find all the verilog/SV files in the directory
                file_path = os.path.join(root, file_name) #To ad the file name to the path
                
                control = control_sig_detector(file_path, file_name)
                total_asset_in_path.extend(control)
                
                status = status_sig_detector(file_path, file_name)
                total_asset_in_path.extend(status)
                
                cnfg = cnfg_sig_detector(file_path, file_name)
                total_asset_in_path.extend(cnfg)
                
                data = data_sig_detector(file_path, file_name)
                total_asset_in_path.extend(data)
                
                param = para_sig_detector(file_path, file_name)
                total_asset_in_path.extend(param)
                
    return total_asset_in_path
                    
        
                    

asset_dataset = asset_detector_individual_file(path)


def append_to_csv(data, file_path):
    header = ['Filename', 'Asset', 'width', 'Signal_type', 'Appeared in', 'CIA']
    
    save_path = Path(file_path)
    output_file = save_path / "asset_list.csv"
    
    # Check if the file already exists
    file_exists = output_file.exists()

    with open(output_file, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)

        if not file_exists:
            writer.writeheader()

        for row in data:
            if len(row) == 6:
                writer.writerow({
                    'Filename': row[4].lower(),  # or .capitalize(), etc.
                    'Asset': row[0],
                    'width': row[1],
                    'Signal_type': row[2],
                    'Appeared in': row[3],
                    'CIA': row[5]
                })
                                    
append_to_csv(asset_dataset, path)
print(f" asset_list.csv has been saved to '{path}' directory")
                    