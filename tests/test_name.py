"""
Your Name: Nikki Tebaldi
Class: CS 521 - Summer 2
Date: 08/18/2019
Term Project

Test Name Unittest Module: Tests Name class methods.

Classes:
    TestMovie(unittest.TestCase): Test methods and functions from Name 
        class.

Class Methods:
    test_str(self): Test the __str__ method.
    test_repr(self): Test that the __repr__ method.
    test_get_full_name(self): Test the get_full_name method.
"""

import unittest
from Name import Name

class TestName(unittest.TestCase):
    """ Test methods from Name class """
    
    def test_str(self):
        """ 
        Test that str method returns a string representation of the object.
        """
        
        # Create a Name object and get the full name
        name = Name("Iain", "Robert", "Pears")
        
        # Assert expected result of the str function
        self.assertEqual(str(name), ("First Name: Iain\nMiddle Name: Robert"\
            "\nLast Name: Pears"))
        
    def test_repr(self):
        """ 
        Test that the repr method returns an official representation of the
        object as a string.
        """
        
        # Create a Name object and get the full name
        name = Name("Iain", "Robert", "Pears")
        
        # Assert expected result of the repr function
        self.assertEqual(repr(name), ("Name('Iain', 'Robert', 'Pears')"))
    
    def test_get_full_name(self):
        """ 
        Test that get_full_name method returns a string with the first 
        middle, and last name separated by a space
        """
        
        # Create a Name object and get the full name
        name = Name("Iain", "Robert", "Pears")
        full_name = name.get_full_name()
        
        # Assert expected result of the get_full_name function
        self.assertEqual(full_name, ("Iain Robert Pears"))
        
    
if __name__ == "__main__":
    
    unittest.main()