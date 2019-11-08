"""
Your Name: Nikki Tebaldi
Class: CS 521 - Summer 2
Date: 08/18/2019
Term Project

Edit Module: Contains functions that facilitate editing the library 
catalog; either adding or deleting a record.

Functions:
    generate_uid(resource_list): Generate a new unique ID (UID).
    get_resource_type(): Returns valid resource type from user input.
    get_year(): Returns valid year from user input.
    get_country(): Returns valid country from user input.
    get_length(): Returns valid length from user input.
    get_names: Returns valid names from user input.
    get_rating: Returns valid rating from user input.
    get_resource(resource_type): Returns a dictionary of resource data obtained
        from user input.
    get_keywords(): Obtain a list of keywords that describe the resource.
    get_book(uid): Creates and returns a list of book data.
    get_movie(uid): Creates and returns a list of movie data.
    check_resource_exists(resource_list, resource_data): Check if the resource 
        already exists.
    write_resource_record(resource): Writes one resource record.
    write_keywordsc_record(resource): Writes one keywords records.
    create_type_specific_record(resource): Writes either book or movie data.
    write_names_record(resource, name_type): Writes inidividual names with UID.
    create_record(resource_list): Prompts for information from user to add a 
        new record.
    create_names_list(name_objects): Takes a list of Name objects and returns a 
        list of strings.
    write_resource_csv(file_path, resource_list): Writes Resource objects.
    write_keywords_csv(file_path, resource_list): Writes keywords.
    write_book_csv(resource_list, csv_file): Write book data.
    write_movie_csv(resource_list, csv_file): Write movie data.
    write_cast_csv(resource_list, csv_file): Write cast data.
    write_writers_csv(resource_list, csv_file): Write writers data.
    write_resources_to_csv_files(resource_list): Write resources to files.
    select_resource_by_uid(resource_list): Allow user to select resource by UID.
    delete_resource(resource_to_delete, resource_list): Writes resource list 
        without the resource parameter.
    remove_record(resource_list): Removes record from CSV files.
"""

from browse import display_collection_by_title_table
from create_resource_lists import create_name_object
from file_management import get_csv_path, write_dict_to_csv,\
write_list_to_csv
from search import search_for_title
import datetime

def generate_uid(resource_list):
    """
    Generate a new unique ID (UID). 
    
    UIDs for resrouce records are incremented by one based off of the last resource
    entered. The last resource will always have hte highest UID number.
    
    Parameters:
        resource_list (list): List of Resource objects; either Book or Movie
    
    Returns:
        (int): Unique integer ID number
    """
    
    uid_list = []
    
    # Create a list of uids
    for resource in resource_list:
        
        uid_list.append(resource.get_uid())
        
    # Sort the list
    uid_list.sort()
    
    # Increment the last uid by 1 as the uids are generated in numerical order
    return uid_list[-1] + 1

def get_resource_type():
    """ 
    Prompt for a resource type and validates user input.
    
    Returns:
        resource_type (str): The type of resource
    """
    
    valid = False
    
    while not valid:
        
        resource_type = input("\nWhat type of resource do you want to add?"\
                              "\n    Enter 'Book' or 'Movie': ").lower()
        
        if resource_type == "book" or resource_type == "movie":
            
            valid = True
        
        else:
            
            print("\n'{0}' is invalid. Please enter input again.\n"
                  .format(resource_type))
            
            valid = False
            
    return resource_type

def get_year():
    """
    Obtain a valid year for the resource.
    
    Returns:
        year (int): 4-digit integer that represents a year
    """

    valid = False
        
    while not valid:
        
        year = input("\nYEAR\n(enter 4 digits): ")
        
        if len(year) != 4:
            
            print("\n'{0}' is an invalid year. Please enter a year with "\
                  "4 digits.\n".format(year))
            
            continue
        
        try:
            
            year = int(year)
            
            valid = True
        
        except ValueError:
            
            print ("'{0}' is not a number. Please enter a year with "\
                   "4 digits.\n".format(year))
            
            continue
            
        if year < 1440 or year > datetime.datetime.now().year:
            
            print("\n{0} is not within the expected year range of 1440 to {1}. "\
                  "Please enter year within this range.\n"
                  .format(year, datetime.datetime.now().year))
            
            valid = False
                
    return year

def get_country():
    """
    Obtain a the country in which the resource was created in.
    
    Returns:
        (string): 2 character code representing the country
    """
    
    valid = False
    
    while not valid:
    
        country = input("\nCOUNTRY\n(two letter abbreviation for country): ")
        
        if len(country) != 2:
            
            print("\nYou did not enter a two letter abbreviation for country. "\
                  "\nPlease try again.\n")
        
        else:
            
            valid = True
            
    return country

def get_length():
    """
    Gets the length of the resource and returns it as a float value.
    
    Returns:
        length (float): The length of a resource
    """
    
    valid = False
    
    while not valid:
        
        length = input("\nLENGTH\n(enter a decimal value): ")
            
        try:
            
            length = float(length)
            
            valid = True
        
        except:
            
            print ("'{0}' is not a number. Please enter a number.\n"
                   .format(length))
                
    return length

def get_names():
    """ 
    Obtains a list of names.
    
    Returns:
        (list): List of names
    """
    
    input_list = input("(enter a list of names "\
                       "[first_name middle_name last_name] \nseparated by a "\
                       "comma): ").split(',')
                      
    # Strip out spaces before and after names
    for i in range(len(input_list)):
        
        input_list[i] = input_list[i].strip()
    
    return input_list

def get_rating():
    """
    Obtains a movie's MPAA rating.
    
    Returns:
        (string): Letter(s) representing MPAA rating
    """
    
    # List out ratings
    MPAA = ['G', 'PG', 'PG-13', 'R', 'NC-17']
    
    valid = False
    
    # Loop until a rating from the MPAA list is obtained
    while not valid:
    
        rating = input("\nRATING\n(enter MPAA rating): ").upper()
    
        if rating not in MPAA:
            
            print("\n'{0}' is not a valid rating. \nPlease enter a rating "\
                  "from the following list: \n\t G, PG, PG-13, R, NC-17)"
                  .format(rating))
            
        else:
        
            valid = True
    
    return rating
    
def get_resource(resource_type):
    """
    Prompt for data pertaining to a resource and returns a dictionary of
    obtained resource data.
    
    Parameters:
        resource_type (str): Type of resource; either "book" or "movie"
    
    Returns:
        (dict): Dictionary of resource data; keys are the data attributes' names
        and values are the resource's data
    """
    
    # Get resource data
    title = input("\nTITLE\n(the title of the resource): ")
    
    creator = input("\nCREATOR\n(the name of the creator): ")
    
    summary = input("\nSUMMARY\n(a summary of the resource): ")
    
    genre = input("\nGENRE\n(one or two words that describe the resource): ")
    
    language = input("\nLANGUAGE\n(the language of the resource): ")
    
    year = get_year()
    
    country = get_country()
    
    length = get_length()
    
    # Return resource data
    return {"Title": title, "Creator": creator, "Summary": summary, 
            "Genre": genre, "Language": language, "Year": year, 
            "Country": country, "Length": length, "Type": resource_type}
    
def get_keywords():
    """
    Obtain a list of keywords that describe the resource.
    
    Returns:
        (list): List of keywords
    """
    
    # Obtain a list of keywords
    keywords = input("\nKEYWORDS\n(enter a list of keywords separated by a "\
                     "comma): ").strip().split(", ")
    
    # Return keywords list
    return keywords
        
def get_book(uid):
    """
    Prompts for data pertaining to a book and returns a list of book data.
    
    Parameters:
        uid (int): Unique ID for book
    
    Returns:
        (dictionary): Dictionary of book data
    """
    
    publisher = input("\nPUBLISHER\n(name of the publisher): ")
    city = input("\nCITY\n(name of the city the book was published in): ")
    category = input("\nCATEGORY\n(one word that describes the type of "\
                     "\nbook [e.g. fiction, nonfiction, etc.]): ")
    
    return {"UID": uid, "Publisher": publisher, "City": city, 
            "Cateogry": category}

def get_movie(uid):
    """
    Prompts for data pertaining to a book and returns a list of movie data.
    
    Parameters:
        uid (int): Unique ID for book
    
    Returns:
        (dictionary): Dictionary of movie data
    """
    
    # Obtain movie data
    rating = get_rating()
    
    # Return list of movie data
    return {"UID": uid, "Rating": rating}

def check_resource_exists(resource_list, resource_data):
    """
    Check if the resource already exists by comparing: title, creator, language,
    year, country, length, type.
    
    Parameters:
        resource_list (list): List of Resource objects; either Book or Movie
        resource_data (dictionary): Dictionary of resource data
    
    Returns:
        exists (Boolean): Whether the resource exists in the resource list
    """
    
    # Assume the resource does not exist in the list until found
    exists = False
    
    for resource in resource_list:
        
        # Construct creator's name
        d_name = resource_data["Creator"]
        
        d_name = create_name_object(d_name)
        
        if resource.title.lower() == resource_data["Title"].lower() \
        and resource.creator.get_full_name() == d_name.get_full_name().lower()\
        and resource.language.lower() == resource_data["Language"].lower() \
        and resource.year == resource_data["Year"] \
        and resource.country.lower() == resource_data["Country"].lower() \
        and resource.resource_type.lower() == resource_data["Type"].lower():
        
            exists = True
    
    return exists

def write_resource_record(resource):
    """
    Writes one record to the Resources.csv file.
    
    Parameters:
        resource_list(Resource): Resource object; either Book or Movie
    """
    
    # Obtain correct csv file path for resources
    file_path = get_csv_path("Resource.csv")
    
    # Write resource record
    write_dict_to_csv(file_path, resource, 'a')
    
def write_keywords_record(resource):
    """
    Obtain a list of keywords for the resource and write to Keywords CSV file.
    
    Parameters:
        resource (Resource): Resource object; either Book or Movie
    """
    
    # Get keywords for resource
    keywords = get_keywords()
    
    # Obtain correct csv file path for resources
    file_path = get_csv_path("Keywords.csv")
    
    # Write resource record
    write_list_to_csv(file_path, keywords, resource["UID"], 'a')
    
def create_type_specific_record(resource):
    """
    Obtain data pertaining to either a Book or Movie resource and write data to
    either the Book.csv file or the Movie.csv file.
    
    Parameters:
        resource (Resource): Resource object; either Book or Movie
    """
    
    if resource["Type"] == "book":
            
        # Get book data
        book = get_book(resource["UID"])
               
        # Obtain correct csv file path for books
        file_path = get_csv_path("Book.csv")
        
        # Write resource record
        write_dict_to_csv(file_path, book, 'a')
        
    else:
        
        # Get movie data
        movie = get_movie(resource["UID"])
        
        # Obtain correct csv file path for movies
        file_path = get_csv_path("Movie.csv")
    
        # Write resource record
        write_dict_to_csv(file_path, movie, 'a')
        
def write_names_record(resource, name_type):
    """
    Writes inidividual names with UID to appropriate csv files which would
    either be Cast.csv or Writers.csv.
    
    Parameters:
        resource (Resource): Resource object; either Book or Movie
        name_type (string): The type of name (writers or cast)
    """
    
    print("\n{0}".format(name_type.upper()))
    
    names = get_names()
    
    # Obtain correct csv file path for cast
    file_path = get_csv_path(name_type.capitalize() + ".csv")

    # Write resource record
    write_list_to_csv(file_path, names, resource["UID"], 'a')

def create_record(resource_list):
    """
    Prompts for information from user to add a new record to the library
    catalog.
    
    Parameter:
        resource_list (list): List of Resource objects; either Book or Movie
        
        Returns:
            modified (bool): Whether CSV files have been modified
    """
    
    # Get valid resource type
    resource_type = get_resource_type()
    
    # Generate a unique UID
    uid = generate_uid(resource_list)
        
    # Add uid to resource dictionary
    resource = {"UID": uid}
    
    # Get resource data
    resource.update(get_resource(resource_type))
    
    # Check to see if the resource already exists
    exists = check_resource_exists(resource_list, resource)
    
    if not exists:
        
        # Resource
        write_resource_record(resource)
           
        # Keywords
        write_keywords_record(resource)
        
        # Book or Movie
        create_type_specific_record(resource)
        
        if resource["Type"] == "movie":
        
            # Cast
            write_names_record(resource, 'cast')     
    
            # Writers
            write_names_record(resource, 'writers')
            
        modified = True
        
        print("\nRecord has been saved.")
    
    # Resource already exists        
    else:
        
        modified = False
        
        print("\nResource already exists.")
    
    return modified

def create_names_list(name_objects):
    """
    Takes a list of Name objects and returns a list of strings that
    represent the Name objects.
    
    Parameters:
        name_objects (list): List of Name objects
        
    Returns:
        names_strings (list): List of names as strings
    """
    
    # Initalize a list to hold the name strings
    name_strings = []
    
    # Loop through each Name object
    for name in name_objects:
        
        name_strings.append(name.get_full_name())
    
    return name_strings
        
    
def write_resource_csv(file_path, resource_list):
    """
    Writes Resource objects contained in the resource list to file at file path.
    
    Parameters:
        file_path (string): Path to csv file
        resource_list (list): List of Resource objects; either Book or Movie
    """
    
    # Write initial record to overwrite CSV file
    dictionary = {"UID": resource_list[0].get_uid(), 
                  "Title": resource_list[0].title, 
               "Creator": resource_list[0].creator.get_full_name(), 
               "Summary": resource_list[0].summary, 
               "Genre": resource_list[0].genre,
               "Language": resource_list[0].language, 
               "Year": resource_list[0].year, 
               "Country": resource_list[0].country, 
               "Length": resource_list[0].length,
               "Type": resource_list[0].resource_type}
    
    write_dict_to_csv(file_path, dictionary, 'w')
    
    # Loop through each resource and create a list to write to csv file
    for i in range(1, len(resource_list)):
        
        dictionary = {"UID": resource_list[i].get_uid(),
                      "Title": resource_list[i].title,
                      "Creator": resource_list[i].creator.get_full_name(),
                      "Summary": resource_list[i].summary,
                      "Genre": resource_list[i].genre,
                      "Language": resource_list[i].language,
                      "Year": resource_list[i].year,
                      "Country": resource_list[i].country,
                      "Length": resource_list[i].length,
                      "Type": resource_list[i].resource_type}
        
        write_dict_to_csv(file_path, dictionary, 'a')
        
def write_keywords_csv(file_path, resource_list):
    """
    Writes keywords to file at file path parameter from resource
    list.
    
    Parameters:
        file_path (string): Path to csv file
        resource_list (list): List of Resource objects; either Book or Movie
    """
    
    fieldnames = ["UID", "Keywords"]
    
    # Write initial row with fieldnames to overwrite file
    write_list_to_csv(file_path, resource_list[0].keywords, 
                      resource_list[0].get_uid(), 'w', fieldnames)
    
    for i in range(1, len(resource_list)):
        
        write_list_to_csv(file_path, resource_list[i].keywords, 
                          resource_list[i].get_uid(), 'a')
        
def write_book_csv(resource_list, csv_file):
    """
    Write book data to Book.csv file
    
    Parameters:
        resource_list (list): List of resource objects; either Book or Movie
        csv_file (string): File path to CSV file
    """
    
    # Keep track of whether a record should be written or appended
    book_written = False
    
    # Loop through each resource
    for i in range(len(resource_list)):
        
        if resource_list[i].resource_type == "book":
            
            # No record has been written yet
            if book_written == False:
                
                # Overwrite file
                file_mode = 'w'
            
            else:
                
                # Append to end of file
                file_mode = 'a'
            
            # Write book data
            dictionary = {"UID": resource_list[i].get_uid(),
                          "Publisher": resource_list[i].publisher,
                          "City": resource_list[i].city,
                          "Category": resource_list[i].category}
            
            write_dict_to_csv(csv_file, dictionary, file_mode)
            
            # Resource has been writetn
            book_written = True
            
def write_movie_csv(resource_list, csv_file):
    """
    Write movie data to Movie.csv file
    
    Parameters:
        resource_list (list): List of resource objects; either Book or Movie
        csv_file (string): File path to CSV file
    """
    
    # Keep track of whether a record should be written or appended
    movie_written = False
    
    # Loop through each resource
    for i in range(len(resource_list)):
    
        if resource_list[i].resource_type == "movie":
                
                # No record has been written yet
                if movie_written == False:
                    
                    # Overwrite file
                    file_mode = 'w'
                
                else:
                    
                    # Append to end of file
                    file_mode = 'a'
               
                # Write movie data
                dictionary = {"UID": resource_list[i].get_uid(), 
                              "Rating": resource_list[i].rating}
            
                write_dict_to_csv(csv_file, dictionary, file_mode)
                
                # Resource has been writetn
                movie_written = True

def write_cast_csv(resource_list, csv_file):
    """
    Write cast data to Cast.csv file
    
    Parameters:
        resource_list (list): List of resource objects; either Book or Movie
        csv_file (string): File path to CSV file
    """
    
    cast_fieldnames = ["UID", "Cast"]
       
    # Keep track of whether a record should be written or appended
    cast_written = False
    
    # Loop through each resource
    for i in range(len(resource_list)):
        
        # Test if resource is a movie
        if resource_list[i].resource_type == "movie":
            
            # No record has been written yet
            if cast_written == False:
                
                # Overwrite file
                file_mode = 'w'
            
            else:
                
                # Append to end of file
                file_mode = 'a'
            
            # Create list of cast names    
            cast_list = create_names_list(resource_list[i].cast)
            
            # Write cast data to csv
            write_list_to_csv(csv_file, cast_list,resource_list[i].get_uid(), 
                              file_mode, cast_fieldnames)
            
            cast_written = True
        
def write_writers_csv(resource_list, csv_file):
    """
    Write writers data to Writers.csv file
    
    Parameters:
        resource_list (list): List of resource objects; either Book or Movie
        csv_file (string): File path to CSV file
    """
    
    writer_fieldnames = ["UID", "Writers"]
       
    # Keep track of whether a record should be written or appended
    writers_written = False
    
    # Loop through each resource
    for i in range(len(resource_list)):
        
        # Test if resource is a movie
        if resource_list[i].resource_type == "movie":
            
            # No record has been written yet
            if writers_written == False:
                
                # Overwrite file
                file_mode = 'w'
            
            else:
                
                # Append to end of file
                file_mode = 'a'
            
            # Create list of writers names    
            writers_list = create_names_list(resource_list[i].writers)
            
            # Write writers data
            write_list_to_csv(csv_file, writers_list, 
                          resource_list[i].get_uid(), file_mode, 
                          writer_fieldnames)
            
            writers_written = True
                           
def write_resources_to_csv_files(resource_list):
    """ 
    Write resource list parameter to appropriate CSV files.
    
    Parameters:
        resource_list (list): List of Resource objects; either Book or Movie
        
    Returns:
        (bool): Whether the CSV files were modified
    """
    
    # Obtain resource csv file path
    resource_file_path = get_csv_path("Resource.csv")
    
    # Write to resource csv file
    write_resource_csv(resource_file_path, resource_list)
    
    # Obtain keywords csv file path
    keywords_file_path = get_csv_path("Keywords.csv")
    
    # Write keywords to csv file
    write_keywords_csv(keywords_file_path, resource_list)
    
    # Obtain book csv file path
    book_file_path = get_csv_path("Book.csv")
    
    # Write book data to csv dile
    write_book_csv(resource_list, book_file_path)
    
    # Obtain movie csv file path
    movie_file_path = get_csv_path("Movie.csv")
    
    # Write movie data to csv file
    write_movie_csv(resource_list, movie_file_path)
    
    # Obtain cast csv file path
    cast_file_path = get_csv_path("Cast.csv")
    
    # Write cast data to csv file
    write_cast_csv(resource_list, cast_file_path)
    
    # Obtain writers csv file path
    writers_file_path = get_csv_path("Writers.csv")
    
    # Write cast data to csv file
    write_writers_csv(resource_list, writers_file_path)
    
def select_resource_by_uid(resource_list):
    """
    Display resources and ask user to select resource that they would like to
    delete. Returns user-selected resource.
    
    Parameters:
        resource_list (list): List of Resource objects; either Book or Movie
        
    Returns:
        resource_to_delete (Resource): Resource object; either Book or Movie
    """
    
    display_collection_by_title_table(resource_list)
    
    user_uid = input("\nPlease enter the UID for the resource you would "\
                     "like to delete: ")
    
    # Set to None until find resource to delete by UID
    resource_to_delete = None
    
    for resource in resource_list:
        
        if resource.get_uid() == int(user_uid):
            
            resource_to_delete = resource
            
            # Found resource to delete break out of for loop
            break
    
    return resource_to_delete

def delete_resource(resource_to_delete, resource_list):
    """
    Writes resource list without the resource parameter to appropriate CSV 
    files.
    
    Parameters:
        resource_to_delete (Resource): Resource object; either Book or Movie
        resource_list (list): List of Resource objects; either Book or Movie
    """
    
    edited_resource_list = []
                
    for resource in resource_list:
        
        if resource.get_uid() == resource_to_delete.get_uid():
            
            continue
        
        else:
            
            edited_resource_list.append(resource)
        
    write_resources_to_csv_files(edited_resource_list)
        
    print("\nResource: '{0}' has been deleted."
          .format(resource_to_delete.title))
    
def remove_record(resource_list):
    """
    Removes record from CSV files.
    
    The user searches for the title of the resource and if found, is prompted
    to remove record.
    
    Parameters:
        resource_list (list): List of Resource objects; either Book or Movie
        
    Returns:
        modified (bool): Whether the CSV files have been modified
    
    """
    
    #Obtain title
    title = input("\nEnter resource title: ")
    
    # Search for resource
    found_resources = search_for_title(title, resource_list)
    
    # More than one resource has been found
    if len(found_resources) >= 2:
        
        resource = select_resource_by_uid(found_resources)
                
    # One resource has been found
    elif len(found_resources) == 1:
        
        resource = found_resources[0]
    
    # No resources have been found
    else:
        
        resource = None
    
    # Resoucre found
    if resource:
        
        # Delete resource
        delete_resource(resource, resource_list)
        
        # Changes have been made
        modified = True
        
    
    # No resources have been found
    else:
        
        print("\nResource not found. No records have been deleted.")
        
        # No changes have been made
        modified = False
        
        
    return modified
        
    
    