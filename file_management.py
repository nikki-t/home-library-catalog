"""
Your Name: Nikki Tebaldi
Class: CS 521 - Summer 2
Date: 08/18/2019
Term Project 

File Management Module: Functions that facilitate reading and writing to
CSV files.

Functions:
    get_csv_path(filename): Returns the full path to the filename.
    get_list_from_csv(csv_path, resource_type=""): Creates a list of sublists
        from a CSV file.
    write_dict_to_csv(file_path, record_dict, file_mode): Write the record 
        dictionary to the file path.
    write_list_to_csv(file_path, record_list, uid, file_mode, fieldnames=[]):
        Write the values contained in the record list to the file path.
"""

import csv
import os

def get_csv_path(filename):
    """
    Creates a file path and returns the full path to the filename.
    
    Parameters:
        filename (str): Name of a file
        
    Returns:
        file_path (str): Path to the filename
    """
    
    # Obtain the file path for the filename
    path = os.getcwd()
    
    file_path = os.path.join(path, "csv", filename)
    
    return file_path

def get_list_from_csv(csv_path, resource_type=""):
    """
    Create a list of sublists from a CSV file with the first sublist containing
    the column names of the csv file.
    
    Parameters:
        csv_path (str): Path to the CSV file
        type (str): Optional type of resource
        
    Returns:
        lst (list): List of sublists with each sublist containing a row from the
        csv file.
    """
    
    # Create a list of lists that contains all of the rows in the csv file
    with open(csv_path) as csv_file:
        
        # Create a list to hold records
        lst = []
        
        # Keep track of line count
        line_count = 0
        
        # Create a reader object to iterate over each line in the csv file
        csv_reader = csv.reader(csv_file, delimiter=",", dialect="excel")
        
        # Loop through lines in the reader object
        for row in csv_reader:
            
            # Create a list of column names at the first index of the list
            if line_count == 0:
                
                lst.append(row)
                
                line_count += 1
            
            # Append the remaining rows to the list depending on the type
            else:
                
                # Determine if reading Resource.csv data and what type of 
                # resource expected in return list
                if "Resource" in csv_path:
                    
                    if row[9] == resource_type.lower():
                    
                        lst.append(row)
                    
                    else:
                    
                        continue
                
                # Not reading Resource.csv so resource type does not matter;
                # just append rows    
                else:
                    
                    lst.append(row)
                    
                
                line_count += 1
    
    return lst

def write_dict_to_csv(file_path, record_dict, file_mode):
    """
    Write the record dictionary as a row to the CSV file represented by
    the file path.
    
    Parameters:
        filepath (string): Full path to a CSV file
        record_dict (dictionary): Dictionary that contains a row of data
        file_mode (string): Single character indicating the mode the file
        should be opened in
    """
    
    # Generate a list of keys
    fieldnames = list(record_dict.keys())
    
    # Open CSV file
    with open(file_path, file_mode) as csv_file:
        
        csv_dict_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        # Write column names if in write mode
        if file_mode == 'w':
            
            csv_dict_writer.writeheader()
        
        csv_dict_writer.writerow(record_dict)
    
def write_list_to_csv(file_path, record_list, uid, file_mode, fieldnames=[]):
    """
    Write the values contained in the record list to the CSV file
    represented by the file path.
    
    Parameters:
        file_path (string): File path to CSV file
        record_dict (list): List of record data
        uid (int): Unique ID
        file_mode (string): Single character indicating the mode the file
        should be opened in
        field_names (list): List of column names; default is an empty list
    """      
    
    with open(file_path, file_mode) as csv_file:
               
        csv_writer = csv.writer(csv_file, dialect="excel", delimiter=',')
        
        # Make sure to write column names to file
        if file_mode == 'w':
            
            csv_writer.writerow(fieldnames)
        
        # Loop through each value in the record list and write a row to the csv
        # file
        for record in record_list:
            
            csv_writer.writerow([uid, record])      
            