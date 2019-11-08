"""
Your Name: Nikki Tebaldi
Class: CS 521 - Summer 2
Date: 08/18/2019
Term Project

Resource Module: A class that represents a resource.

Classes:
    Resource: A class that represents a resource.
    
Class Methods:
    __str__(self): Returns a string representation of a Resource object's state.
    __repr__(self):  Returns an official representation of a Resource object.
    get_uid(self): Return Resource uid (int)
    get_brief_summary(self): Returns a shorter version of the summary attribute.
    get_runtime_in_hours(self): Calculates the runtime in hours and minutes.
    get_keyword_string(self): Returns a list of keywords in alphabetical order.
"""

import copy

class Resource:
    """
    This is a class to represent a generic resource (e.g. book or movie)
    
    Attributes:
        uid (int): Unique resource ID (private)
        title (string): Title of the resource
        creator (Name): Name of the creator of the resource
        summary (string): Summary of the content of the resource
        genre (string): Genre that the resource belongs to
        language (string): Language of the resource
        year (int): Year the resource was created
        country (string): Country that the resource was created in
        length (float): Length of the resource
        resource_type (string): Type of resourcel; either book or movie
        keywords (list): Keywords that represent the resource
        
    Methods:
        __str__(self): Returns a string representation of a Resource object's 
            state
        __repr__(self):  Returns an official representation of a Resource object
        get_uid(self): Return Resource uid (int)
        get_brief_summary(self): Returns a shorter version of the summary 
            attribute
        get_runtime_in_hours(self): Calculates the runtime in hours and minutes
        get_keyword_string(self): Returns a list of keywords in alphabetical 
            order
    """
    
    def __init__(self, uid, title, creator, summary, genre, 
                 language, year, country, length, resource_type, keywords):
        """
         The constructor for the Resource class
         
        Attributes:
            uid (int): Unique resource ID (private)
            title (string): Title of the resource
            creator (Name): Name of the creator of the resource
            summary (string): Summary of the content of the resource
            genre (string): Genre that the resource belongs to
            language (string): Language of the resource
            year (int): Year the resource was created
            country (string): Country that the resource was created in
            length (float): Length of the resource
            resource_type (string): Type of resourcel; either book or movie
            keywords (list): Keywords that represent the resource
        """
        
        self.__uid = uid
        self.title = title
        self.creator = creator
        self.summary = summary
        self.genre = genre
        self.language = language
        self.year = year
        self.country = country
        self.length = length
        self.resource_type = resource_type
        self.keywords = keywords
    
    def __str__(self):
        """ Returns a string representation of a Resource object's state """
        
        # Obtain the value of length depending on resource type
        if self.resource_type == "book":
            
            length = str(round(self.length)) + "p"
            
        else:
            
            hours, minutes = self.get_runtime_in_hours()
            
            length = str(round(hours)) + "h " + str(round(minutes)) + "m"
        
        # Return string representative of Resource objects state
        return "ID: {0} \nTitle: {1} \nCreator: {2} \nSummary: {3} "\
            "\nGenre: {4} \nLanguage: {5} \nYear: {6} \nCountry: {7} "\
            "\nLength: {8} \nType: {9} \nKeywords: {10}".format(self.__uid, 
            self.title, self.creator.get_full_name(), self.get_brief_summary(),
            self.genre, self.language, self.year, self.country, length, 
            self.resource_type, self.get_keyword_string())
    
    def __repr__(self):
        """ Returns an official string representation of a Resource object """

        return "Resource({0}, '{1}', {2}, '{3}', '{4}', '{5}', {6}, '{7}', "\
            "{8}, '{9}', '{10}')".format(self.__uid, self.title, 
            repr(self.creator), self.summary, self.genre, self.language, 
            self.year, self.country, self.length, self.resource_type,
            self.keywords)
            
    def get_uid(self):
        """ Return Resource uid (int) """
        
        return self.__uid
    
    def get_brief_summary(self):
        """
        If the summary is greater than 150 characters, shorten the summary so
        that it is 147 characters plus "..." to indicate the summary continues.
        
        Return:
            brief_summary (string): A shortened version of the summary that is 
            150 characters
        """
        
        # Split the summary into words
        words = self.summary.split()
    
        # Initialize a string to hold a brief version of the summary
        brief_summary = ""
        
        # Keep track of line length
        line_length = 70
        
        # Loop through each word and add it to brief_summary plus a new line
        # if the line is over 80 characters
        for word in words:
            
            brief_summary += word + " " 
            
            if len(brief_summary) >= line_length:
                
                brief_summary += "\n"
                
                line_length += 70
                
        # Determine if the length of brief summary is greater than 150      
        if len(brief_summary) > 150:
            
            # Indicate that the summary continues
            brief_summary = brief_summary[:147] + "..."
                
        return brief_summary
    
    def get_runtime_in_hours(self):
        """ 
        Calculate the runtime in hours and minutes that is entered in minutes.
        
        Note that length's unit of measurement is in minutes for
        movies.
        
        Returns:
            runtime (tuple): Tuple where hours is stored in index 0 and minutes
            is stored at index 1
        """
        
        hours = self.length // 60
        minutes = self.length % 60
        
        return (hours, minutes)

    def get_keyword_string(self):
        """ 
        Returns a string that contains the contents of the keyword list sorted
        in alphabetical order.
            
        Returns:
            lst_string (string): String that contains all the elements in the
            keyword list
        """
        
        # Grab a copy of the keywords list so it is not altered
        kw_list = copy.copy(self.keywords)
        
        kw_list.sort()
        
        # Create a sequence string from parameter sequence
        lst_string = ""
        
        for item in kw_list:
            
            lst_string += str(item) + ", "
        
        # Return string with ending comma and space removed
        return lst_string[:-2]