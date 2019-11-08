"""
Your Name: Nikki Tebaldi
Class: CS 521 - Summer 2
Date: 08/18/2019
Term Project

Search Module: Functions that facilitate searching the library 
catalog by keyword or title.

Functions:
    match_uid_with_resource(uid_list, resource_list): Return a list that 
        contains Resource objects matched with UIDs.
    search_for_keyword(word, resource_list): Searches for a keyword in the 
        resource list. 
    search_for_title(title, resource_list): Searches the resource list for the 
        title and returns a list of Resource objects.
"""

from create_resource_lists import get_keywords, get_uids_from_list

def match_uid_with_resource(uid_list, resource_list):
    """
    Return a list that contains Resource objects that match the UIDs present
    in the UID list.
    
    Parameters:
        uid_list (list): List of integer unique IDs
        resource_list (list): List of Resource objects; either Book or Movie
    
    Returns:
        found_resources (list): List of Resource object; either Book or Movie
        that match the UIDs present in the UID list.
    """
    
    # Search for uid in resource list and if found append to a new list
    found_resources = []
    
    for resource in resource_list:
    
        for uid in uid_list:

            if int(uid) == resource.get_uid():
                
                found_resources.append(resource)
                
    return found_resources

def search_for_keyword(word, resource_list): 
    """
    Searches for a keyword in the resource list. 
    
    If the keyword is found, the function returns a list of resources that
    contain the keyword otherwise the function returns a list of None.
    
    Parameters:
        word (string): Keyword to search for
        resource_list (list): List of Resource objects; either Book or Movie
    
    Returns:
        keyword_resources (list): List of Resource objects or a list of None 
    """
    
    # Get a list of keywords associated with uids
    keywords_list = get_keywords()
    
    # Initialize list with column names to store lists that contain found word
    found_list = [keywords_list[0]]
    
    for lst in keywords_list:
        
        for keywords in lst:
            
            if word in keywords:
                
                found_list.append(lst)
                
                # Found word; can continue searching another record
                continue
    
    # Locate resources associated with keyword if any resources are found
    found_resources = []
    
    if found_list:
        
        # Obtain a list of UIDs
        uid_list = get_uids_from_list(found_list)
        
        # Obtain a list of resources matched with found UIDs
        found_resources = match_uid_with_resource(uid_list, resource_list)
    
    return found_resources

def search_for_title(title, resource_list):
    """
    Searches the resource list for the title and returns a list of Resource
    objects with the title if the title is found otherwise returns None.
    
    Note: Two or more resources can have the same title.
    
    Parameters:
        title (str): Title of a resource
        resource_list (list): List of Resource objects; either Book or Movie
        
    Returns:
        found_list (Resource): A list of Resource objects either Book or 
        Movie or an empty list
    """
    
    # Initialize a list to hold resources that contain the title 
    found_list = []
    
    # Loop through reosurce list and if found assign the resource object to
    # found_resource variable
    for resource in resource_list:
        
        if title.strip().lower() == resource.title.strip().lower():
            
            found_list.append(resource)
    
    # Return list of found_resources
    return found_list
            