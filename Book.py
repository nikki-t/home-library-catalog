"""
Your Name: Nikki Tebaldi
Class: CS 521 - Summer 2
Date: 08/18/2019
Term Project

Book Module: Represents a book which is a subclass of resource.

Classes:
    Book(Resource): A subclass of Resource.
    
Class Methods:
    __str__(self): Returns a string representation of a Book object's state.
    __repr__(self):  Returns an official representation of a Book object.
"""

from Resource import Resource

class Book(Resource):
    """
    This is a class that represents a book and is a subclass of Resource
    
    Attributes:
        publisher (string): The name of the publisher of the book
        city (string): Where the book was published
        category (string): A string that best categorizes the type of book
        
    Methods:
        __str__(self): Returns a string representation of a Book object's state
        __repr__(self):  Returns an official representation of a Book object
    """
    
    def __init__(self, publisher, city, category, *args):
        """
        The constructor for the Book class
        
        Attributes: 
            publisher (string): The name of the publisher of the book
            city (string): Where the book was published
            category (string): A string that best categorizes the type of book
        """
        
        super().__init__(*args)
        self.publisher = publisher
        self.city = city
        self.category = category
    
    def __str__(self):
        """ Returns a string representation of a Book object's state """
        
        return super().__str__() + "\nPublisher: {0} \nCity: {1} "\
            "\nCategory: {2}".format(self.publisher, self.city, self.category)
    
    def __repr__(self):
        """ Returns an official string representation of a Book object """
        
        # Alter Resource class repr function to fit Book class
        super_repr = super().__repr__()
        
        # Remove 'Resource' and closng parenthesis
        super_repr = super_repr[9:len(super_repr) - 1]
        
        return "Book({0}, '{1}', '{2}', '{3}')".format(super_repr, 
                                                       self.publisher, 
                                                       self.city, self.category)