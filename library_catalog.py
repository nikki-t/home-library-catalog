"""
Your Name: Nikki Tebaldi
Class: CS 521 - Summer 2
Date: 08/18/2019
Term Project

Library Catalog Module: Main program of the library catalog; largely menu-driven
as action is taken based on user choice.

Functions:
    get_resource_list(): Obtain list of resources.
    display_main_menu(): Display the main menu.
    display_browse_menu(): Display the browse menu.
    display_search_menu(): Display the search menu.
    display_edit_menu(): Display the edit menu.
    print_invalid_range_message(choice): Display an invalid range message.
    get_valid_menu_choice(): Obtains a valid menu choice from the user.
    browse_collection(resource_list): Browses the collection based on user 
        input.
    search_collection(resource_list): Searches the collection based on user 
        input.
    edit_collection(resource_list): Edits the collection based on user 
        input.
    run_library_catalog(): The main function to display and manipulate a small 
     library catalog.
"""

from browse import display_collection_by_title_record, \
display_collection_by_title_table
from create_resource_lists import get_book_list, get_movie_list
from edit import create_record, remove_record
from search import search_for_keyword, search_for_title
import sys

def get_resource_list():
    """
    Obtain list of resources.
    
    Returns:
        resource_list (list): List of Resource objects; either Book or Movie
    """
    
    # Try to construct a list of resources from both movies and books
    try:
        
        resource_list = get_book_list() + get_movie_list()
    
    # File containing resource data is not found and program will exit.
    except FileNotFoundError as error:
        
        print("File Not Found: {0}. Program exit.".format(error))
        
        sys.exit(1)
        
    except ValueError as error:
        
        print("Data type error: Cannot load library catalog. \n\n\tPlease try "\
              "restoring files.\n\nProgram exit.")
        
        sys.exit(1)
        
    except IndexError as error:
        
        print("Index error: Cannot loading library catalog. \n\n\tPlease try "\
              "restoring files. \n\nProgram exit.")
        
        sys.exit(1)
    
    return resource_list
    

def display_main_menu():
    """ Display the main menu """
    
    print("LIBRARY CATALOG")
    print("Main Menu:")
    print("----------")
    print("1. Browse")
    print("2. Search")
    print("3. Edit")
    print("4. Exit Program")
    print()
    
def display_browse_menu():
    """ Display a menu of browse choices """
    
    print()
    print("Browse Menu:")
    print("------------")
    print("1. Browse by Record")
    print("2. Browse by Table")
    print("3. Exit Browse")
    print()
    
def display_search_menu():
    """ Display a menu of search choices """
    
    print()
    print("Search Menu:")
    print("------------")
    print("1. Search by Keyword")
    print("2. Search by Title")
    print("3. Exit Search")
    print()
    
def display_edit_menu():
    """ Display a menu of edit choices """
    
    print()
    print("Edit Menu:")
    print("------------")
    print("1. Add a Record")
    print("2. Delete a Record")
    print("3. Exit Edit")
    print()
    
def print_invalid_range_message(choice):
    """
    Display an invalid range message
    
    Parameters:
        choice (int): Invalid user choice
    """
    
    print("\n'{0}' is not within the expected range." \
          "\nPlease enter input again.".format(choice))
    
def get_valid_menu_choice():
    """
    Validates user input of numeric menu choice.
    
    Returns:
        user_choice (int): Numeric choice for menu selection
    """
    
    while True:
        
        # Obtain user input
        user_choice = input("Please enter a numeric value as your choice: ")
        
        # Try to conver input to an integer
        try:
            
            user_choice = int(user_choice)
            
            # User input is numeric; break out of while loop
            break
            
        except ValueError:
            
            print("\n'{0}' is not numeric input. Please try"\
                  " again.\n".format(user_choice))
    
    return user_choice

def browse_collection(resource_list):
    """ 
    Displays a browse menu and takes action based on user input.
    
    Parameters:
        resource_list (list): List of Resource objects either Book or Movie
    
    Returns:
        proceed (Boolean): Indicates if the user would like to continue
    """
    
    display_browse_menu()
            
    browse_choice = get_valid_menu_choice()

    if browse_choice == 1:
    
        display_collection_by_title_record(resource_list)
        
        print("\n\tReturning to 'Browse Menu'...")
        
        proceed = True
        
    
    elif browse_choice == 2:
    
        display_collection_by_title_table(resource_list)
        
        print("\n\tReturning to 'Browse Menu'...")
        
        proceed = True
    
    elif browse_choice == 3:
        
        # Exit
        proceed = False

    else:
    
        print_invalid_range_message(browse_choice)
        
        proceed = True
        
    return proceed

def search_collection(resource_list):
    """ 
    Displays a search menu and takes action based on user input.
    
    Parameters:
        resource_list (list): List of Resource objects either Book or Movie
    
    Returns:
        proceed (Boolean): Indicates if the user would like to continue
    """
    
    display_search_menu()
            
    search_choice = get_valid_menu_choice()

    if search_choice == 1:
        
        # Obtain keyword from user
        word = input("\nEnter a keyword to search for: ").lower()
        
        found_resources = search_for_keyword(word, resource_list)
        
        # Display the resources that were found
        if found_resources:
            
            print("\nResources that contain '{0}':".format(word))
            print("============================================")
            
            display_collection_by_title_record(found_resources)
            print("\n\tReturning to 'Search Menu'...")
        
        else:
            
            print("\nNo resources contained the keyword: '{0}'".format(word))
            print("\n\tReturning to 'Search Menu'...")
        
        proceed = True
        
    
    elif search_choice == 2:
    
        # Obtain title for user
        title = input("\nEnter a title to search for: ")
        
        found_resources = search_for_title(title, resource_list)
        
        # Display the resources that were found
        if found_resources:
            
            print("\nResources with the title '{0}':".format(title))
            print("===============================================")
            
            display_collection_by_title_record(found_resources)
            print("\n\tReturning to 'Search Menu'...")
        
        else:
            
            print("\nNo resources contained the title: '{0}'".format(title))
            print("\n\tReturning to 'Search Menu'...")
        
        proceed = True
    
    elif search_choice == 3:
        
        # Exit
        proceed = False

    else:
    
        print_invalid_range_message(search_choice)
        
        proceed = True
        
    return proceed

def edit_collection(resource_list):
    """ 
    Displays an edit menu and takes action based on user input.
    
    Parameters:
        resource_list (list): List of Resource objects either Book or Movie
    
    Returns:
        proceed (Boolean): Indicates if the user would like to continue
        reload_records (Boolean): Indicates whether the resource list should
        be repopulated as csv files have been modified
    """
    
    display_edit_menu()
            
    edit_choice = get_valid_menu_choice()

    if edit_choice == 1:
        
        reload_records = create_record(resource_list)
            
        print("\n\tReturning to 'Edit Menu'...")
        
        proceed = True
        
    
    elif edit_choice == 2:
    
        reload_records = remove_record(resource_list)
    
        print("\n\tReturning to 'Edit Menu'...")
        
        proceed = True
    
    elif edit_choice == 3:
        
        # No changes made to records
        reload_records = False
        
        proceed = False

    else:
    
        print_invalid_range_message(edit_choice)
        
        # Exit; no changes made to records
        reload_records = False
        
        proceed = True
        
    return proceed, reload_records

def run_library_catalog():
    """
    This is the main function to display and manipulate a small library catalog
    """
    
    # Obtain the list of resources present in the catalog
    resource_list = get_resource_list()
    
    # Initialize value to control while loop for actions taken based on user
    # input
    exit_menu = False
    
    while not exit_menu:
        
        # Display menu choices
        display_main_menu()
        
        # Obtain valid menu choice as an integer value
        user_choice = get_valid_menu_choice()
        
        # Take action based on user choice
        if user_choice == 1:
            
            browse = True
            
            while browse:
                
                browse = browse_collection(resource_list)
            
            # Done browsing return to main menu:
            print("\nReturning to main menu...\n")
        
        elif user_choice == 2:
            
            search = True
            
            while search:
                
                search = search_collection(resource_list)
                
            # Done browsing return to main menu:
            print("\nReturning to main menu...\n")
        
        elif user_choice == 3:
            
            edit = True
            
            while edit:
                
                edit, reload = edit_collection(resource_list)
                
                # If records have been saved, need to reload resource_list with
                # updated changes
                if reload:
            
                    resource_list = get_resource_list()
            
            # Done browsing return to main menu:
            print("\nReturning to main menu...\n")
        
        elif user_choice == 4:
            
            # Exit
            exit_menu = True
        
        else:
            
            print_invalid_range_message(user_choice)
            
    print("\nProgam exit.\n")

if __name__ == "__main__":
    
    run_library_catalog()