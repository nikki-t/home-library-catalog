"""
Your Name: Nikki Tebaldi
Class: CS 521 - Summer 2
Date: 08/18/2019
Term Project

Test Book Unittest Module: Tests Book class methods.

Classes:
    TestResource(unittest.TestCase): Test methods and functions from Resource 
        class.

Class Methods:
    test_str(self): Test the __str__ method.
    test_repr(self): Test that the __repr__ method.
"""

import unittest
from Book import Book
from Name import Name

class TestResource(unittest.TestCase):
    """ Test methods from Resource class"""
    
    def test_str(self):
        """ 
        Test that str method returns a string representation of the object.
        """
        
        # Create a Resource object
        book = Book("Penguin Group", "New York", "fiction", 1, "White Noise", 
                    Name("Don", "", "DeLillo"), 
                    "Delillo's White Noise follows narrator Jack "\
                    "Gladney, a professor at a small Liberal Arts "\
                    "college and describes an academic year. Jack "\
                    "teaches at a school called the "\
                    "College-on-the-Hill, where he serves as the "\
                    "department chair of Hitler studies. He lives in "\
                    "Blacksmith, a quiet college town, with his wife, "\
                    "Babette, and four of their children from earlier "\
                    "marriages: Heinrich, Steffie, Denise, and "\
                    "Wilder. Throughout the novel, various "\
                    "half-siblings and ex-spouses drift in and out "\
                    "of the family’s home.",
                    "sci-fi", "English", 1985, "US", 326, "book",
                    ["culture", "survival", "life", "society"])
        
        # Assert expected result of the str function
        self.assertEqual(str(book), ("ID: 1 \nTitle: White Noise "\
            "\nCreator: Don DeLillo \nSummary: Delillo's White Noise follows "\
            "narrator Jack Gladney, a professor at a \nsmall Liberal Arts "\
            "college and describes an academic year. Jack teaches \nat ... "\
            "\nGenre: sci-fi \nLanguage: English \nYear: 1985 "\
            "\nCountry: US \nLength: 326p \nType: book "\
            "\nKeywords: culture, life, society, survival\nPublisher: "\
            "Penguin Group \nCity: New York \nCategory: fiction"))
        
    def test_repr(self):
        """
        Test that the repr method returns an official representation of the
        object as a string.
        """
        
        # Create a Resource object
        book = Book("Penguin Group", "New York", "fiction", 1, "White Noise", 
                    Name("Don", "", "DeLillo"), 
                    "Delillo's White Noise follows narrator Jack "\
                    "Gladney, a professor at a small Liberal Arts "\
                    "college and describes an academic year. Jack "\
                    "teaches at a school called the "\
                    "College-on-the-Hill, where he serves as the "\
                    "department chair of Hitler studies. He lives in "\
                    "Blacksmith, a quiet college town, with his wife, "\
                    "Babette, and four of their children from earlier "\
                    "marriages: Heinrich, Steffie, Denise, and "\
                    "Wilder. Throughout the novel, various "\
                    "half-siblings and ex-spouses drift in and out "\
                    "of the family’s home.",
                    "sci-fi", "English", 1985, "US", 326, "book",
                    ["culture", "survival", "life", "society"])
    
        
        # Assert expected result of the repr function
        self.assertEqual(repr(book), ("Book(1, 'White Noise', "\
                            "Name('Don', '', 'DeLillo'), "\
                            "'Delillo's White Noise follows narrator Jack "\
                            "Gladney, a professor at a small Liberal Arts "\
                            "college and describes an academic year. Jack "\
                            "teaches at a school called the "\
                            "College-on-the-Hill, where he serves as the "\
                            "department chair of Hitler studies. He lives in "\
                            "Blacksmith, a quiet college town, with his wife, "\
                            "Babette, and four of their children from earlier "\
                            "marriages: Heinrich, Steffie, Denise, and "\
                            "Wilder. Throughout the novel, various "\
                            "half-siblings and ex-spouses drift in and out "\
                            "of the family’s home.', 'sci-fi', 'English', "\
                            "1985, 'US', 326, 'book', "\
                            "'['culture', 'survival', 'life', 'society']', "\
                            "'Penguin Group', 'New York', 'fiction')"))
        
if __name__ == "__main__":
    
    unittest.main()