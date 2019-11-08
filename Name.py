"""
Your Name: Nikki Tebaldi
Class: CS 521 - Summer 2
Date: 08/18/2019
Term Project

Name Module: Represents a person's full name.

Classes:
    Name: A class that represents a person's full name.
    
Class Methods:
    __str__(self): Returns a string representation of a Name object's state.
    __repr__(self):  Returns an official representation of a Name object.
    get_full_name(self): Create a string that contains the first name, 
        middle name, and the last name.
"""

class Name:
    """
    A class that represents a name
    
    Attributes:
        first (str): First name
        middle (str): Middle name
        last (str): Last name
    
    Methods:
        __str__(self): Returns a string representation of a Name object's state
        __repr__(self):  Returns an official representation of a Name object
        get_full_name(self): Create a string that contains the first name, 
            middle name, and the last name
    """
    
    def __init__(self, first, middle="", last=""):
        """
        The constructor for Name class.
        
        Does not require the use of a middle or last name.
        
        Parameters:
            first (str): First name
            middle (str): Middle name
            last (str): Last name
        """
        
        self.first = first
        self.middle = middle
        self.last = last
        
    def __str__(self):
        """ Returns a string representation of a Name object's state """
        
        return "First Name: {0}\nMiddle Name: {1}"\
            "\nLast Name: {2}".format(self.first, self.middle, self.last)
    
    def __repr__(self):
        """ Returns an official string representation of a Name object """
        
        return "Name('{0}', '{1}', '{2}')".format(self.first, self.middle, 
                                                  self.last)
        
    def get_full_name(self):
        """
        Create a string that contains the first name, middle name, and the last
        name separated by a space
        
        Returns:
            full_name(string): The first, middle and last name seperated by a 
            space
        """
        
        # There is only one name
        if self.middle == "" and self.last =="":
            
            full_name = "{0}".format(self.first)
        
        # There are three names
        elif self.middle != "" and self.last != "":
            
            full_name = "{0} {1} {2}".format(self.first, self.middle, self.last)
        
        # There are two names    
        else:
            
            full_name = "{0} {1}".format(self.first, self.last)
            
        return full_name