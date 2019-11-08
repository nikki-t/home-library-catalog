"""
Your Name: Nikki Tebaldi
Class: CS 521 - Summer 2
Date: 08/18/2019
Term Project

Browse: A Module that contains functions that facilitate browsing a library
catalog.

Functions:
    sort_collection_by_title(resource_list): Sort the collection by alphabetical
        order by title.
    display_collection_by_title_record(resource_list): Displays the collection 
        in record format.
    display_collection_by_title_table(resource_list): Displays the collection in
        table format.
"""

def sort_collection_by_title(resource_list):
    """
    Sort the collection in alphabetical order by title using a instertion sort
    algorithm.
    
    Parameters:
        resource_list (list): A list of resources
        
    Returns:
        resource_list(list): A list of resources sorted by title
    """
    
    # Loop through resource_list
    for i in range(len(resource_list)):
        
        # Store current element in resource list
        current_element = resource_list[i]
        
        # Initialize another index value for comparison
        k = i - 1
        
        # Compare the titles of the current element and the element found at 
        # index k
        while k >= 0 and resource_list[k].title > current_element.title:
            
            # Insert the element found at index k into the element found at 
            # k + 1
            resource_list[k + 1] = resource_list[k]
            
            k -= 1
        
        # Insert current element at k + 1 after completing index comparisons    
        resource_list[k + 1] = current_element
        
    return resource_list

def display_collection_by_title_record(resource_list):
    """
    Displays the collection in record format organized in alphabetical order
    by title.
    
    Parameters:
        resource_list (list): List of Resource objects either Book or Movie
    """
    
    # Obtain sorted resource_list
    resource_list = sort_collection_by_title(resource_list)
    
    # initialize a variable to keep track of number of resources displayed
    resource_count = 0
    
    # Loop through the list and display each record
    print()   # Separate output from main menu
    for resource in resource_list:
        
        print(resource, "\n")
        
        resource_count += 1
        
        # Display two records and then pause display; ask user to hit enter 
        # to continue
        if resource_count % 2 == 0:
            
            if resource_count == len(resource_list):
            
                continue
            
            input("\nPress 'Enter' to continue record display.\n")
            
def display_collection_by_title_table(resource_list):
    """ 
    Displays the collection in table format organized in alphabetical order
    by title.
    
    Not all resource data is displayed. The table display is meant to show all 
    resources in the collection in an easy to read manner.
    
    Parameters:
        resource_list (list): List of Resource objects either Book or Movie
    """
    
    # Obtain sorted resource_list
    resource_list = sort_collection_by_title(resource_list)
    
    # Display type
    print("\nBOOKS:")
    print("======")
    
    # Display column names
    print("{:7s} {:30s} {:20s} {:11s} {:9s} {:5s} {:8s} {:14s}"\
          " {:9s} {:18s} {:20s}"
          .format("UID", "Title", "Creator", "Genre", "Language", "Year", 
                 "Country",  "Publisher", "City", "Category", 
                 "Keywords"))
    
    # Display book resources
    for resource in resource_list:
        
        if resource.resource_type == "book":

            print("{:<7d} {:30s} {:20s} {:11s} {:9s} {:<5d} {:8s} {:14s} "\
                  "{:9s} {:18s} {:20s}"
                  .format(resource.get_uid(), resource.title[:29], 
                          resource.creator.get_full_name(), resource.genre[:10], 
                          resource.language[:8], resource.year, 
                          resource.country, resource.publisher[:13], 
                          resource.city, resource.category,
                          resource.get_keyword_string()))

    # Display type
    print("\nMOVIES:")
    print("=======")
    
    # Display column names
    print("{:7s} {:30s} {:20s} {:11s} {:9s} {:5s} {:8s} {:7s} {:35s} {:20s}"
          .format("UID", "Title", "Creator", "Genre", "Language", "Year", 
                 "Country", "Rating", "Writers", "Keywords"))
    
    # Display movie resources
    for resource in resource_list:
        
        if resource.resource_type == "movie":
            
            print("{:<7d} {:30s} {:20s} {:11s} {:9s} {:<5d} {:8s} {:7s} "\
                  "{:35s} {:20s}"
                  .format(resource.get_uid(), resource.title, 
                          resource.creator.get_full_name(), 
                          resource.genre, resource.language[:8], resource.year, 
                          resource.country, resource.rating, 
                          resource.get_names_string(resource.writers)[:35], 
                          resource.get_keyword_string()))