"""
Your Name: Nikki Tebaldi
Class: CS 521 - Summer 2
Date: 08/18/2019
Term Project

Book Module: Represents a movie which is a subclass of resource.

Classes:
    Movie(Resource): A subclass of Resource.
    
Class Methods:
    __str__(self): Returns a string representation of a Movie object's state.
    __repr__(self):  Returns an official representation of a Movie object.
    get_names_string(self, names): Create a string of a list of names. 
"""

from Resource import Resource

class Movie(Resource):
    """
    A class to represent a movie which is a subclass of Resource
    
    Attributes:
        rating (string): The MPAA rating
        writers (list): List of Name objects that contain the names of writers
        cast (list): List of Name objects that contain the names of the cast
        
    Methods:
        __str__(self): Returns a string representation of a Movie object's state
        __repr__(self):  Returns an official representation of a Movie object
        get_names_string(self, names): Create a string of a list of names
    """
    
    def __init__(self, rating, writers, cast, *args):
        """ The constructor of the Movie class
        
        Attributes:
            rating (string): The MPAA rating
            writers (list): List of Name objects that contain the names of writers
            cast (list): List of Name objects that contain the names of the cast
        """
        
        super().__init__(*args)
        self.rating = rating
        self.writers = writers
        self.cast = cast
        
    def __str__(self):
        """ Returns a string representation of a Movie object's state """
        
        # Create a string of writers
        writers_str = self.get_names_string(self.writers)
                
        # Create a string of cast members
        cast_str = self.get_names_string(self.cast)
        
        return super().__str__() + "\nRating: {0} \nWriters: {1}"\
            "\nCast: {2} ".format(self.rating, writers_str, cast_str)
            
    def __repr__(self):
        """ Returns an official string representation of a Book object """
        
        # Alter Resource class repr function to fit Book class
        super_repr = super().__repr__()
        
        # Remove 'Resource' and closng parenthesis
        super_repr = super_repr[9:len(super_repr) - 1]
        
        return "Movie({0}, '{1}','{2}', '{3}'".format(super_repr, self.rating,
                                                      self.writers, self.cast)
    
    def get_names_string(self, names):
        """ 
        Create a string that contains a list of names from the list parameter.
        
        Parameters:
            names (list): A list of Name objects
        
        Returns:
            (string): A string that contains a list of names
                
        """
        
        # Define a seperator for each name
        name_sep = ", "
        
        # Get  a list of names in string form from the names parameter
        name_list = [name.get_full_name() for name in names]
        
        # Return the list of names separated by a comma and a space
        return name_sep.join(name_list)