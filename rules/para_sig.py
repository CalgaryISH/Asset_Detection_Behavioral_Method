# -----------------------------------------------------------------------------
# File Name: para_sig.py
# Version: 0.1
# Author: Subroto Kumer Deb Nath
# Email: subroto.ece.ku@gmail.com
# Description: Detects asset related to parameter signals from individual
#              Verilog/SystemVerilog file along with CIA tag, and width
# Copyright (c) 2025 Subroto Kumer Deb Nath
# This file is part of an open-source project and is released under the MIT License.
# You are free to use, modify, and distribute this file with proper attribution.
# -----------------------------------------------------------------------------


import re
import os
def extract_parameters_bit(file_path):
    names = []
    numbers = []

    # Regular expression to match "parameter bit <name> = <number>"
    pattern = r'parameter bit\s+(\w+)\s*=\s*(\d+)'

    with open(file_path, encoding="utf8") as file:  #SystemVerilog is a UTF8 encoded file
        lines = file.readlines()
        for i, line in enumerate(lines, start=1):
            line = line.strip()
            line = line.lower()
            
            match = re.search(pattern, line)
            if match:
                name = match.group(1)  # Extract the name
                number = match.group(2)  # Extract the number
                names.append(name)
                numbers.append(int(number))  # Convert the number to an integer
    
    return names

def parameters(line):
    """
    Extracts all parameter or localparam names from a single line of Verilog/SystemVerilog.
    Returns a list of parameter names.
    """
    # Check if line starts with parameter/localparam (with optional width)
    header = re.match(r'\s*(parameter|localparam)\b(?:\s*\[[^\]]+\])?', line)
    if not header:
        return []

    # Remove the header part to handle multiple parameters
    line_body = re.sub(r'^\s*(parameter|localparam)\b\s*(\[[^\]]+\]\s*)?', '', line)
    # Find all parameter names before '='
    names = re.findall(r'(\w+)\s*=', line_body)
    return names

def parameter_extractor(file_path):
    param = []
    with open(file_path, encoding="utf8") as file:  #SystemVerilog is a UTF8 encoded file
        lines = file.readlines()
        for i, line in enumerate(lines, start=1):
            line = line.strip()
            line = line.lower()
            name = parameters(line)
            if (len(name) > 0): 
                param.extend(name)
    return param
                
                

def para_sig_detector(file_path, file_name):
    
    param_bit = []
    param = []
    param_sig = []

    param_bit = extract_parameters_bit(file_path)
    param = parameter_extractor(file_path)
    
    for item in param_bit:
        sig_details = [item, "1-bit", "Param", "parameter bit", file_name, "A"]
        param_sig.append(sig_details)
    for item in param:
        sig_details = [item, "multi-bit", "Param", "parameter", file_name, "I"]
        param_sig.append(sig_details)
                    
                    

    return param_sig



