# -----------------------------------------------------------------------------
# File Name: control_sig.py
# Version: 0.1
# Author: Subroto Kumer Deb Nath
# Email: subroto.ece.ku@gmail.com
# Description: Detects asset related to control signals from individual
#              Verilog/SystemVerilog file along with CIA tag, and width
# Copyright (c) 2025 Subroto Kumer Deb Nath
# This file is part of an open-source project and is released under the MIT License.
# You are free to use, modify, and distribute this file with proper attribution.
# -----------------------------------------------------------------------------


import os
import re
from collections import Counter


# final_ios = []
#Final Input Extractor

def extract_input_signals_from_code(code):
    # Remove all comments (single and multi-line)
    code = re.sub(r'//.*?$|/\*.*?\*/', '', code, flags=re.DOTALL | re.MULTILINE)

    # Find all input declarations in the code
    # Handles: input [width] type name1, name2, ...;
    #          input type name1, name2, ...;
    #          input name1, name2, ...;
    # Handles multi-line and inline with other signals
    input_pattern = re.compile(
        r'\binput\b'                          # input keyword
        r'(?:\s+\w+)*'                        # optional type (logic, wire, reg, user-defined, etc.)
        r'(?:\s*\[[^]]*\])?'                  # optional width [msb:lsb]
        r'((?:\s+\w+\s*,?)+)',                # signal names, possibly comma separated
        re.IGNORECASE | re.MULTILINE
    )

    signals = []
    for match in input_pattern.finditer(code):
        names = match.group(1)
        for sig in names.split(','):
            sig = sig.strip()
            # only add valid signal names
            if sig and re.match(r'^[a-zA-Z_]\w*$', sig):
                signals.append(sig)
    return signals

def final_in(file_path):
    input_signals = []
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        code = f.read()
        signals = extract_input_signals_from_code(code)
        input_signals.extend(signals)
    return sorted(set(input_signals))

def extract_inputs(file_path):
    inputs = []
    with open(file_path, encoding="utf8") as file:  #SystemVerilog is a UTF8 encoded file
        lines = file.readlines()

        for i, line in enumerate(lines, start=1): 
            line = line.strip()
            line = line.lower()
            if line.startswith("input") and "?" not in line and "//" in line:
                if "logic" not in line:
                    info, rest = line.split("//", 1)
                    if ';' in info and ',' not in info:
                        
                        words = info.split()
                        if words:
                            inputs.append(words[-1].rstrip(';'))
                    elif ',' in info and ';' not in info:
                        
                        words = info.split()
                        if words:
                            for item in words:
                                
                                if ',' in item:
                                    x = item.replace(',', '')
                                    inputs.append(x)
                                    
                                elif '' in item and 'input' not in item:
                                    x = item.replace('', '')
                                    inputs.append(x)
                    elif ',' in info and ';' in info:
                        
                        words = info.split()
                        if words:
                            for item in words:
                                
                                if ',' in item:
                                    x = item.replace(',', '')
                                    inputs.append(x)
                                    
                                elif ';' in item:
                                    x = item.replace(';', '')
                                    inputs.append(x)
                    
                    
                    elif ';' not in info and ',' not in info:
                        words = info.split()
                        if words:
                            inputs.append(words[-1])
                elif "logic" in line:
                    new_line = line.replace('logic', '')
                    info, rest = new_line.split("//", 1)
                    if ';' in info and ',' not in info:
                        
                        words = info.split()
                        if words:
                            inputs.append(words[-1].rstrip(';'))
                    elif ',' in info and ';' not in info:
                        
                        words = info.split()
                        if words:
                            for item in words:
                                
                                if ',' in item:
                                    x = item.replace(',', '')
                                    inputs.append(x)
                                    
                                elif '' in item and 'input' not in item:
                                    x = item.replace('', '')
                                    inputs.append(x)
                    elif ',' in info and ';' in info:
                        
                        words = info.split()
                        if words:
                            for item in words:
                                
                                if ',' in item:
                                    x = item.replace(',', '')
                                    inputs.append(x)
                                    
                                elif ';' in item:
                                    x = item.replace(';', '')
                                    inputs.append(x)
                    
                    
                    elif ';' not in info and ',' not in info:
                        words = info.split()
                        if words:
                            inputs.append(words[-1])
                        
            elif line.startswith("input") and "?" not in line and "//" not in line:
                if "logic" not in line:
                    info = line
                    if ';' in info and ',' not in info:
                        
                        words = info.split()
                        if words:
                            inputs.append(words[-1].rstrip(';'))
                    elif ',' in info and ';' not in info:
                        
                        words = info.split()
                        if words:
                            for item in words:
                                
                                if ',' in item:
                                    x = item.replace(',', '')
                                    inputs.append(x)
                                    
                                elif '' in item and 'input' not in item:
                                    x = item.replace('', '')
                                    inputs.append(x)
                    elif ',' in info and ';' in info:
                        
                        words = info.split()
                        if words:
                            for item in words:
                                
                                if ',' in item:
                                    x = item.replace(',', '')
                                    inputs.append(x)
                                    
                                elif ';' in item:
                                    x = item.replace(';', '')
                                    inputs.append(x)
                    
                    
                    elif ';' not in info and ',' not in info:
                        words = info.split()
                        if words:
                            inputs.append(words[-1])
                        
                elif "logic" in line:
                    
                    info = line.replace('logic', '')
                    if ';' in info and ',' not in info:
                        
                        words = info.split()
                        if words:
                            inputs.append(words[-1].rstrip(';'))
                    elif ',' in info and ';' not in info:
                        
                        words = info.split()
                        if words:
                            for item in words:
                                
                                if ',' in item:
                                    x = item.replace(',', '')
                                    inputs.append(x)
                                    
                                elif '' in item and 'input' not in item:
                                    x = item.replace('', '')
                                    inputs.append(x)
                    elif ',' in info and ';' in info:
                        
                        words = info.split()
                        if words:
                            for item in words:
                                
                                if ',' in item:
                                    x = item.replace(',', '')
                                    inputs.append(x)
                                    
                                elif ';' in item:
                                    x = item.replace(';', '')
                                    inputs.append(x)
                    
                    
                    elif ';' not in info and ',' not in info:
                        words = info.split()
                        if words:
                            inputs.append(words[-1])            
                         

    return inputs

def count_items(input_list):
    # Count the frequency of each item in the list
    item_counts = Counter(input_list)
    
    # Create a list of tuples with each item and its frequency
    result_list = [[item, count] for item, count in item_counts.items()]
    
    return result_list


def extract_signals_types(code):
    # Regular expressions to match the different types of signals
    control_signal_pattern = re.compile(r'\bif\s*\(\s*(\w+)\s*\)')
    assigned_signal_pattern = re.compile(r'\b(\w+)\s*(?:<=|=)\s*')
    driving_signal_pattern = re.compile(r'(?:<=|=)\s*(\w+);')

    # Find all control signals
    control_signal_matches = control_signal_pattern.findall(code)
    control_signals = list(set(control_signal_matches))  # Removing duplicates

    # Find all assigned signals
    assigned_signal_matches = assigned_signal_pattern.findall(code)
    assigned_signals = list(set(assigned_signal_matches))  # Removing duplicates

    # Find all driving signals
    driving_signal_matches = driving_signal_pattern.findall(code)
    driving_signals = list(set(driving_signal_matches))  # Removing duplicates
    
    return control_signals, assigned_signals, driving_signals

def signal_type_extractor(file_path):
    ct_sig = []
    as_sig = []
    dr_sig = []
    with open(file_path, encoding="utf8") as file:  #SystemVerilog is a UTF8 encoded file
        lines = file.readlines()
        for i, line in enumerate(lines, start=1):
            line = line.strip()
            line = line.lower()
            if not line.startswith("//"):
                if "//" in line:
                    info, rest = line.split("//", 1)
                    c, a, d = extract_signals_types(info)
                    if(len(c) > 0):
                        ct_sig.extend(c)
                    if(len(a) > 0):
                        as_sig.extend(a)
                    if(len(d) > 0):
                        dr_sig.extend(d)
                else:
                    c, a, d = extract_signals_types(line)
                    if(len(c) > 0):
                        ct_sig.extend(c)
                    if(len(a) > 0):
                        as_sig.extend(a)
                    if(len(d) > 0):
                        dr_sig.extend(d)
            
    return ct_sig, as_sig, dr_sig

def extract_always_blocks(file_path):
    blocks = []
    current_block = []
    within_always = False
    no_begin = False
    if_check = False
    else_check = False
    within_if = False
    within_else = False
    begin_count = 0
    end_count = 0
    
    with open(file_path, encoding="utf8") as file:  #SystemVerilog is a UTF8 encoded file
        lines = file.readlines()

        for i, line in enumerate(lines, start=1): 
            line = line.strip()
            line = line.lower()
            if (line.startswith('always @') or line.startswith('always@')) and "begin" in line:
                begin_count += line.count('begin')
                end_count += line.count('end')
                within_always = True
                current_block.append(line)
            elif within_always:
                begin_count += line.count('begin')
                end_count += line.count('end')
                current_block.append(line)
                if begin_count == end_count:
                    blocks.append('\n'.join(current_block))
                    current_block = []
                    within_always = False
                    
            elif (line.startswith('always @') or line.startswith('always@')) and "begin" not in line:
                current_block.append(line)
                no_begin = True
            elif no_begin:
                if line.startswith("if (") and "begin" in line:
                    begin_count += line.count('begin')
                    end_count += line.count('end')
                    current_block.append(line)
                    within_if = True
                    
                elif within_if:
                    begin_count += line.count('begin')
                    end_count += line.count('end')
                    current_block.append(line)
                    if begin_count == end_count:
                        blocks.append('\n'.join(current_block))
                        current_block = []
                        within_if = False
                    
                    
                elif line.startswith("if (") and "begin" not in line:
                    current_block.append(line)
                    if_check = True
                    
                elif line.endswith(";") and line.startswith("begin") and if_check == True:
                    begin_count += line.count('begin')
                    end_count += line.count('end')
                    current_block.append(line)
                    within_if = True
                    
                    
                elif line.endswith(";") and not line.startswith("begin") and if_check == True:
                    current_block.append(line)
                    if_check = False
                    
                elif line.startswith("else") and "begin" in line:
                    begin_count += line.count('begin')
                    end_count += line.count('end')
                    current_block.append(line)
                    within_else = True
                    
                elif within_else:
                    begin_count += line.count('begin')
                    end_count += line.count('end')
                    current_block.append(line)
                    if begin_count == end_count:
                        blocks.append('\n'.join(current_block))
                        current_block = []
                        within_else = False
                        
                elif line.startswith("else") and "begin" not in line:
                    current_block.append(line)
                    else_check = True
                    
                elif line.endswith(";") and line.startswith("begin") and else_check == True:
                    begin_count += line.count('begin')
                    end_count += line.count('end')
                    current_block.append(line)
                    within_else = True
                    
                    
                elif line.endswith(";") and not line.startswith("begin") and else_check == True:
                    current_block.append(line)
                    else_check = False
                else:
                    no_begin = False
                    if(len(current_block) > 0):
                        blocks.append('\n'.join(current_block))
                        current_block = []
                
                
                    

    return blocks


def width_calculation_io(code):
    # Regular expression to detect I/O and widths
    io_port_regex = re.compile(
        r'\b(input|output|inout)\b\s*(\b(?:reg|wire)\b\s*)?(?:\[(\d+):(\d+)\]\s*)?([\w,\s]+?)(?:;|$)',
        re.MULTILINE
    )
    
    # Regular expression to detect reg, wire, and logic nets
    net_regex = re.compile(
        r'\b(reg|wire|logic)\b\s*(?:\[(\d+):(\d+)\]\s*)?([\w,\s]+?)(?:;|$)',
        re.MULTILINE
    )

    signal_info = []
    seen_signals = set()

    for match in io_port_regex.finditer(code):
        width_msb = match.group(3)
        width_lsb = match.group(4)
        port_names = match.group(5)

        if width_msb and width_lsb:
            width = abs(int(width_msb) - int(width_lsb)) + 1
        else:
            width = 1

        # Split port names by comma and strip any extra whitespace
        port_names_list = [name.strip() for name in port_names.split(',')]
        
        for port_name in port_names_list:
            if port_name not in seen_signals:
                if len(port_name)>0:
                    signal_info.append([port_name, width])
                    seen_signals.add(port_name)
    
    for match in net_regex.finditer(code):
        width_msb = match.group(2)
        width_lsb = match.group(3)
        net_names = match.group(4)

        if width_msb and width_lsb:
            width = abs(int(width_msb) - int(width_lsb)) + 1
        else:
            width = 1

        # Split net names by comma and strip any extra whitespace
        net_names_list = [name.strip() for name in net_names.split(',')]
        
        for net_name in net_names_list:
            if net_name not in seen_signals:
                if len(net_name)>0:
                    signal_info.append([net_name, width])
                    seen_signals.add(net_name)

    return signal_info
        
def width_calculator(file_path):
    width_data = []
    with open(file_path, encoding="utf8") as file:  #SystemVerilog is a UTF8 encoded file
        lines = file.readlines()
        for i, line in enumerate(lines, start=1):
            line = line.strip()
            line = line.lower()
            if not line.startswith("//"):
                if "//" in line:
                    info, rest = line.split("//", 1)
                    s_w = width_calculation_io(info)
                    if(len(s_w) > 0):
                        width_data.extend(s_w)
                else:
                    s_w = width_calculation_io(line)
                    if(len(s_w) > 0):
                        width_data.extend(s_w)
            
    return width_data

def extract_blocking_assign(file_path):
    lhs_ba = []
    rhs_ba = []
    
    
    with open(file_path, encoding="utf8") as file:  #SystemVerilog is a UTF8 encoded file
        lines = file.readlines()

        for i, line in enumerate(lines, start=1): 
            line = line.strip()
            line = line.lower()
            if not line.startswith("//"):
                if "//" in line:
                    info, rest = line.split("//", 1)
                    if info.startswith("assign") and "=" in info and ";" in info:
                        extra, data = info.split("assign", 1)
#                         print(data)
                        lhs, rhs = data.split("=", 1)
                        lhs.strip()
                        rhs.strip()
                        
                        if "0;" not in rhs and '\'b' not in rhs and '\'h' not in rhs:
                            lhs_ba.append(lhs)
                            rhs_ba.append(rhs)
                            
                    if not info.startswith("assign") and "=" in info and ";" in info:
                        
                        lhs, rhs = info.split("=", 1)
                        lhs.strip()
                        rhs.strip()
                        
                        if "0;" not in rhs and '\'b' not in rhs and '\'h' not in rhs:
                            lhs_ba.append(lhs)
                            rhs_ba.append(rhs)
                if "//" not in line:
                    
                    if line.startswith("assign") and "=" in line and ";" in line:
                        extra, data = line.split("assign", 1)
                        lhs, rhs = data.split("=", 1)
                        lhs.strip()
                        rhs.strip()
                        
                        if "0;" not in rhs and '\'b' not in rhs and '\'h' not in rhs:
                            lhs_ba.append(lhs)
                            rhs_ba.append(rhs)
                    if not line.startswith("assign") and "=" in line and ";" in line:
                        
                        lhs, rhs = line.split("=", 1)
                        lhs.strip()
                        rhs.strip()
                        
                        if "0;" not in rhs and '\'b' not in rhs and '\'h' not in rhs:
                            lhs_ba.append(lhs)
                            rhs_ba.append(rhs)
                
                
                
    updated_lhs = [item.replace(" ", "") for item in lhs_ba]           
    updated_rhs = [item.replace(" ", "") for item in rhs_ba]
    rhs_ba = [item.replace(";", "") for item in updated_rhs]
    return updated_lhs, rhs_ba

def if_signals(line):
    # Check if the line starts with 'if' or 'else if'
    
        # Extract everything inside the first pair of parentheses
    matches = re.findall(r'\bif\s*\(([^()]*)\)', line)
    if matches:
        # Define a regex pattern to split by logical and comparison operators
        pattern = r'\s*(==|!=|<=|>=|<|>|\|\||&&)\s*'
        # Split the content by the defined pattern
        signals = re.split(pattern, matches[0])
        # Remove '!' and strip any leading/trailing whitespace from each signal
        signals = [signal.replace('!', '').strip() for signal in signals]
        # Filter out any empty strings resulting from splitting
        signals = [signal for signal in signals if signal]
        return signals
    return []


def extract_if_else(file_path):
    if_else_signals = []
    
    
    with open(file_path, encoding="utf8") as file:  #SystemVerilog is a UTF8 encoded file
        lines = file.readlines()

        for i, line in enumerate(lines, start=1): 
            line = line.strip()
            line = line.lower()
            signals = if_signals(line)
            if(len(signals) > 0):
                if_else_signals.extend(signals)
                
    for item in if_else_signals:
        if item == "&&" or item == "rst" or item == "reset" or item == "rst_ni" or item == "||" or item == "==" or item == "=" or item == "!=" or item == ">=" or item == "<=" or item == "<" or item == ">":
            if_else_signals.remove(item)
    
    return if_else_signals




def extract_nblocking_assign(file_path):
    lhs_nba = []
    rhs_nba = []
    
    
    with open(file_path, encoding="utf8") as file:  #SystemVerilog is a UTF8 encoded file
        lines = file.readlines()

        for i, line in enumerate(lines, start=1): 
            line = line.strip()
            line = line.lower()
            if not line.startswith("//"):
                if "//" in line:
                    info, rest = line.split("//", 1)
                    if "<=" in info and ";" in info:
                        lhs, rhs = info.split("<=", 1)
                        lhs.strip()
                        rhs.strip()
                        
                        if "0;" not in rhs and '\'b' not in rhs and '\'h' not in rhs:
                            lhs_nba.append(lhs)
                            rhs_nba.append(rhs)
                if "//" not in line:
                    if "<=" in line and ";" in line:
                        lhs, rhs = line.split("<=", 1)
                        lhs.strip()
                        rhs.strip()
                        
                        if "0;" not in rhs and '\'b' not in rhs and '\'h' not in rhs:
                            lhs_nba.append(lhs)
                            rhs_nba.append(rhs)
                
                
                
    updated_lhs = [item.replace(" ", "") for item in lhs_nba]           
    updated_rhs = [item.replace(" ", "") for item in rhs_nba]
    rhs_nba = [item.replace(";", "") for item in updated_rhs]
    return updated_lhs, rhs_nba

def control_sig_detector(file_path, file_name):
    

    lba = []
    rba = []
    lnba = []
    rnba = []
    width_data = []
    ctrl_sig = []
    
    inputs = final_in(file_path)
    if_else_sig = extract_if_else(file_path)
    
            
#                 counted_list = count_items(if_else_sig)
    sorted_if_else_sig = list(set(if_else_sig))
#                 a_blocks = extract_always_blocks(file_path)
    
#                 for item in a_blocks:
#                     c, a, d = extract_signals_types(item)
#                     ct_sig.extend(c)
#                     as_sig.extend(a)
#                     dr_sig.extend(d)
        
    
    lba, rba = extract_blocking_assign(file_path)
    lnba, rnba = extract_nblocking_assign(file_path)
    
    width_data = width_calculator(file_path)
    
    for item in sorted_if_else_sig:
        if item in inputs:
            for w in width_data:
                if item in w:
                    if w[1] == 1:
                        sig_details = [item, w[1], "Control", "if_else", file_name, "A"]
                        ctrl_sig.append(sig_details)
        elif item not in inputs:
            if item in lba:
                x = lba.index(item)
                if rba[x] in inputs:
                    for w in width_data:
                        if rba[x] in w:
                            if w[1] == 1:
                                sig_details = [rba[x], w[1], "Control", "if_else", file_name, "A"]
                                ctrl_sig.append(sig_details)
                
            if item in lnba:
                
                x = lnba.index(item)
                if rnba[x] in inputs:
                    for w in width_data:
                        if rnba[x] in w:
                            if w[1] == 1:
                                sig_details = [rnba[x], w[1], "Control", "if_else", file_name, "A"]
                                ctrl_sig.append(sig_details)
                            

    return ctrl_sig


