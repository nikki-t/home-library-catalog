"""
Your Name: Nikki Tebaldi
Class: CS 521 - Summer 2
Date: 08/18/2019
Term Project

Create Resource Lists Module: Creates a lists of resources (either books or 
movies).

Functions:
    get_uids_from_list(lst): Locate UIDs and append to a new list.
    associate_uid_with_list(lst, uid_list): Returns a list of sublists for each
       UID.
    get_keywords_for_resource(keyword_list, resource_list): Returns a list of 
        keywords with UIDs.
    create_name_object(name_str): Creates and returns a Name object.
    convert_names_to_objects(lst, list_type): Returns a list with Name objects.
    convert_list_element_to_number(lst, index, list_type): Converts list 
        element to an integer or float.
    get_resources(resource_type): Returns a list of resource objects.
    get_keywords(): Returns a list of keywords.
    get_books(): Returns a list of book data.
    get_movies(): Returns a list of movie data.
    get_writers(): Returns a list of writer data.
    get_cast(): Returns a list of cast data.
    create_records(resource_list, lst, lst_type): Returns a list of records.
    get_book_list(): Returns a list of Book objects.
    get_movie_list(): Returns a list of Movie objects.
"""

from Book import Book
from file_management import get_csv_path, get_list_from_csv
from Movie import Movie
from Name import Name

def get_uids_from_list(lst):
    """
    Locate UIDs at index lst[i][0] and append to a new list. Get rid of any
    duplicated uids.
    
    Parameters:
        lst (list): List that contains UIDs at index [i][0]
        
    Returns:
        (list): A list of UIDs without any duplicates
    """
    
    # Determine UIDs present in lst
    uid_list = []
    
    for i in range(1, len(lst)):
        
        uid_list.append(lst[i][0])
    
    # Get rid of duplicate ids and return list
    return list(set(uid_list))

def associate_uid_with_list(lst, uid_list):
    """
    Returns a list of sublists for each UID.
    
    For each sublist, the UID is at index 0 and all subsequent indexes in the 
    sublist contain data associated with that UID.
    
    For use with a list where the UID is repeated over several sublists and you
    want to associate all values with one UID in one sublist.
    
    Parameters:
        lst (list): List that contains UIDs and assoicated data
        uid_list (list): List of UIDs
        
    Returns:
        new_list (list): List of sublists with UIDs and associated data 
        contained in the same sublist
    """
    
    # Create a new list to hold resources associated with uids
    new_list = []
    # Append column names to list
    new_list.append(lst[0])
    
    # Create a list element for each uid 
    for uid in uid_list:
        
        new_list.append([uid])
    
    # Append resources from the parameter lst to new list that match the uids 
    # present in the new list    
    for i in range(1, len(lst)):
        
        for j in range(len(new_list)):
            
            # UIDs are equal in both lists
            if lst[i][0] in new_list[j]:
                
                # Append the entire list
                new_list[j].append(lst[i][1])
    
    return new_list

def get_keywords_for_resource(keyword_list, resource_list):
    """
    Returns a list of keywords with UIDs based on UIDs in resource list.
    
    Parameters:
        keyword_list (list): List of all keywords for all resources
        resource_list (list): List of resources to get keywords for
        
    Returns:
        keywords_for_resources (list): List of keywords associated with
        resources listed in resource list
    """
    
    # Initialize a list to store UIDs and keywords associated with resources
    keywords_for_resources = []
    
    # Loop through resource list and match UIDs with keywords_list
    for resource in resource_list:
        
        for element in keyword_list:
            
            if resource[0] == element[0]:
                
                keywords_for_resources.append(element)
    
    return keywords_for_resources

def create_name_object(name_str):
    """
    Create a Name object for creators in the resource list and replace string
    version with Name object.
    
    Parameters:
        name_str (string): String version of a name
        
    Returns:
        name_obj (Name): Name object
    """
    
    # Split the name string into a list
    name_str = name_str.split(' ')
    
    # The name string has three names
    if len(name_str) == 3:
        name_obj = Name(name_str[0], name_str[1], name_str[2])
   
    # The name string has two names and will place in first and last name 
    # attributes
    elif len(name_str) == 2:
        name_obj = Name(name_str[0], "", name_str[1])
    
    # The name string has one name
    else:
        name_obj = Name(name_str[0])
        
    return name_obj
    
    
def convert_names_to_objects(lst, list_type):
    """
    Create a Name object for creators in the list and replace string
    version with Name object.
    
    Parameters:
        lst (list): List of resources or a list of name strings
        list_type (str): Type of list to create Name objects for
        
    Returns:
        resource_list (list): List of resources with name strings converted to
        Name objects    
    """
    
    for resource in lst:
        
        if list_type == "creator":
            
            # Skip column name
            if resource[2] == "Creator":
                
                continue
            
            # Create a Name object
            name_obj = create_name_object(resource[2])
        
            # Replace string with Name object
            resource[2] = name_obj
            
        if list_type == "movie":
            
            for element in resource:
                
                # Ignore column names and numeric elements
                if element == "Writers" or element == "Cast" \
                or element == "UID" or element.isdigit():
                    
                    continue
                
                # Find the index of the element
                index = resource.index(element)
                
                # Create a Name object
                name_obj = create_name_object(element)
                
                # Replace the name string a Name object
                resource[index] = name_obj
               
    return lst

def convert_list_element_to_number(lst, index, list_type):
    """
    Converts specified list element at index to an integer or float based on 
    list type.
    
    Parameters:
        lst (list): List of data
        index (int): Index at which to convert element to integer
        list_type (str): Indicates whether the element should be converted to a 
        float or integer (values should be "int" or "float")
        
    Returns:
        lst (list): List with converted integer or float element
    """
    
    # Convert specified index element to an integer
    for item in lst:
        
        #Skip column names
        if item[index].isalpha():
            
            continue
        
        else:
            
            # Convert to integer
            if list_type == "int":
            
                item[index] = int(item[index])
                
            # Convert to float    
            else:
                
                item[index] = float(item[index])
            
    return lst

def get_resources(resource_type):
    """
    Returns a list of resources where each row of the csv file is a sublist of 
    the resource list.
    
    The columns in the csv file are repsent in the first sublist.
    
    Parameters:
        resource_type (string): The type of resource the resource list
        should contain
    
    Returns:
        resource_list (list): List that contains sublists for each row in the
        Resource.csv file
    """
    
    # Obtain the file path for Resource.csv which contains records for all
    # resources
    csv_path = get_csv_path("Resource.csv")
    
    # Obtain a list of resources
    resource_list = get_list_from_csv(csv_path, resource_type)
    
    return resource_list

def get_keywords():
    """
    Creates and returns a list of lists from keywords.csv where all sublists are
    the rows for each UID. 
    
    The first sublist is the column names: UID and keywords
    
    Returns:
        (list): List of sublists that contains the UID at index 0 
        and associated keywords at subsequent indexes 
    """
    
    # Obtain the file path for Keywords.csv which contains records for all
    # resources
    csv_path = get_csv_path("Keywords.csv")
    
    #Obtain the list of keywords
    lst = get_list_from_csv(csv_path)
    
    # Determine UIDs present in lst
    uid_list = get_uids_from_list(lst)
    
    # Obtain and return a list of UIDs associated with each keyword
    return associate_uid_with_list(lst, uid_list)

def get_books():
    """
    Creates and returns a list of lists from Book.csv where all sublists are
    the rows in the csv file. The first sublist is the column names present in
    Books.csv.
    
    Returns:
        book_list (list): List that contains sublists of each row in the
        Book.csv file
    """
    
    # Obtain the file path for Book.csv which contains records for all
    # resources
    csv_path = get_csv_path("Book.csv")
    
    #Obtain the list of books
    book_list = get_list_from_csv(csv_path)
    
    return book_list
    
def get_movies():
    """
    Creates and returns a list of lists from Movie.csv where all sublists are
    the rows in the csv file. The first sublist is the column names present in
    Movie.csv.
    
    Returns:
        movie_list (list): List that contains sublists of each row in the
        Movie.csv file
    """
    # Obtain the file path for Book.csv which contains records for all
    # resources
    csv_path = get_csv_path("Movie.csv")
    
    #Obtain the list of books
    movie_list = get_list_from_csv(csv_path)
    
    return movie_list

def get_writers():
    """
    Creates and returns a list of lists from writers.csv where all sublists are
    the rows for each UID. 
    
    The first sublist is the column names: UID and keywords
    
    Returns:
        (list): List of sublists that contains the UID at index 0 
        and associated writers at subsequent indexes
    """
    
    # Obtain the file path for Writers.csv which contains records for all
    # resources
    csv_path = get_csv_path("Writers.csv")
    
    # Obtain the list of writers
    lst = get_list_from_csv(csv_path)
    
    # Obtain a list of UIDs without duplicates
    uid_list = get_uids_from_list(lst)
    
    # Obtain and return a list of writers associated with a UID
    return associate_uid_with_list(lst, uid_list)

def get_cast():
    """
    Creates and returns a list of lists from Cast.csv where all sublists are
    the rows for each UID. 
    
    The first sublist is the column names: UID and keywords
    
    Returns:
        (list): List of sublists that contains the UID at index 0 
        and associated writers at subsequent indexes
    """
    # Obtain the file path for Cast.csv which contains records for all
    # resources
    csv_path = get_csv_path("Cast.csv")
    
    #Obtain the list of cast members
    lst = get_list_from_csv(csv_path)
    
    # Obtain the list of UIDs without duplicates
    uid_list = get_uids_from_list(lst)
    
    # Obtain and return a list of cast members assocaited with a UID
    return associate_uid_with_list(lst, uid_list)

def create_records(resource_list, lst, lst_type):
    """
    Creates a list of records by concatenating the resource list with the
    list parameter based on UID.
    
    If the list type is a resource, the function loops through each item 
    pertaining to the resource (based on UID) and appends the data item to the
    resource list.
    
    If the list type is a list of names or keywords, the function appends the
    entire keyword list that applies to the resource based on UID.
    
    Parameters:
        resource_list (list): List of resources
        lst (list): List of subclass objects for a Resource object (e.g. 
        book or movie) or a list of keywords
        lst_type (string): Type of list (keyword or type)
        
    Returns:
        resource_list (List): List of resources concatenated together with type
        list by UID
    """
    
    for i in range(1, len(resource_list)):
        
        for j in range(1, len(lst)):
            
            # If the UIDs match
            if str(resource_list[i][0]) == lst[j][0]:
                
                # List type is a resource, loop through list data and append 
                # it to the resource list
                if lst_type == "resource":
                
                    for data in lst[j][1:]:
                        
                        resource_list[i].append(data)
                    
                # List type is a list of names or keywords   
                else:
                        
                    # Append entire list
                    resource_list[i].append(lst[j][1:])
                    
    return resource_list

def get_book_list():
    """
    Creates a list of Book objects with index 0 containing a list of
    column names.
    
    Returns:
        book_list (list): List of Book objects
    """
    # Get resource data
    resources = get_resources("book")
    
    keywords = get_keywords_for_resource(get_keywords(), resources)
    
    books = get_books()
    
    # Convert resource data to appropriate types
    resources = convert_names_to_objects(resources, "creator")
        
    # UID to an integer
    resources = convert_list_element_to_number(resources, 0, "int")

    # Year to an integer
    resources = convert_list_element_to_number(resources, 6, "int")
            
    # Length to a float
    resources = convert_list_element_to_number(resources, 8, "float")
    
    # Concatenate records together based on UID
    resources = create_records(resources, keywords, "list")
    
    resources = create_records(resources, books, "resource")
    
    # Create column list
    resources[0] = ['UID', 'Title', 'Creator', 'Summary', 'Genre',\
                    'Language', 'Year', 'Country', 'Length', 'Type', 'Keywords',\
                    'Publisher', 'City', 'Category']
            
    # Create a list of book objects
    book_list = []
    
    for i in range(1, len(resources)):
        
        # Obtain each argument needed to create a Book object       
        uid = resources[i][0]
        title = resources[i][1]
        creator = resources[i][2]
        summary = resources[i][3]
        genre = resources[i][4]
        language = resources[i][5]
        year = resources[i][6]
        country = resources[i][7]
        length = resources[i][8]
        resource_type = resources[i][9]
        keywords = resources[i][10]
        publisher = resources[i][11]
        city = resources[i][12]
        category = resources[i][13]
        
        
        # Create and append a Book object to the book list    
        book_list.append(Book(publisher, city, category, uid, title, creator, 
                              summary, genre, language, year, country, length, 
                              resource_type, keywords))
        
    return book_list
        
    
def get_movie_list():
    """
    Creates a list of Movie objects with index 0 containing a list of
    column names.
    
    Returns:
        movie_list (list): List of Movie objects
    """
    
    # Get resource data
    resources = get_resources("movie")
    
    keywords = get_keywords_for_resource(get_keywords(), resources)
    
    movies = get_movies()
    
    writers = get_writers()
    
    cast = get_cast()
    
    # Convert resource data to appropriate types
    writers = convert_names_to_objects(writers, "movie")
    
    cast = convert_names_to_objects(cast, "movie")
    
    resources = convert_names_to_objects(resources, "creator")
    
    # UID to an integer
    resources = convert_list_element_to_number(resources, 0, "int")

    # Year to an integer
    resources = convert_list_element_to_number(resources, 6, "int")
            
    # Length to a float
    resources = convert_list_element_to_number(resources, 8, "float")
    
    # Concatenate records together based on UID
    resources = create_records(resources, keywords, "list")
    
    resources = create_records(resources, movies, "resource")  
    
    resources = create_records(resources, writers, "list")
    
    resources = create_records(resources, cast, "list")
    
    # Create column list
    resources[0] = ['UID', 'Title', 'Creator', 'Summary', 'Genre',\
                    'Language', 'Year', 'Country', 'Length', 'Type',\
                    'Keywords', 'Rating', 'Writers', 'Cast']
           
    # Create a list of movie objects
    movie_list = []
    
    for i in range(1, len(resources)):
        
        # Obtain each argument needed to create a Book object       
        uid = resources[i][0]
        title = resources[i][1]
        creator = resources[i][2]
        summary = resources[i][3]
        genre = resources[i][4]
        language = resources[i][5]
        year = resources[i][6]
        country = resources[i][7]
        length = resources[i][8]
        resource_type = resources[i][9]
        keywords = resources[i][10]
        rating = resources[i][11]
        writers = resources[i][12]
        cast = resources[i][13]
        
        # Create and append a Book object to the book list    
        movie_list.append(Movie(rating, writers, cast, uid, title, creator, 
                                summary, genre, language, year, country, 
                                length, resource_type, keywords))
        
    return movie_list