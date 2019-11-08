"""
Your Name: Nikki Tebaldi
Class: CS 521 - Summer 2
Date: 08/18/2019
Term Project

Test Movie Unittest Module: Tests Movie class methods.

Classes:
    TestMovie(unittest.TestCase): Test methods and functions from Movie 
        class.

Class Methods:
    test_str(self): Test the __str__ method.
    test_repr(self): Test that the __repr__ method.
    test_get_names_string(self): Test the get_names_string method.
    test_get_brief_summary_output(self): Test get_brief_summary method output.
    test_get_brief_summary_length(self): Test get_brief_summary method output 
        length.
    test_get_runtime_in_hours(self): Test that get_runtime_in_hours method.
    test_get_keyword_string(self): Test get_keyword_string method.
"""

import unittest
from Name import Name
from Resource import Resource

class TestResource(unittest.TestCase):
    """ Test methods from Resource class"""
    
    def test_str(self):
        """ 
        Test that str method returns a string representation of the object.
        """
        
        # Create a Resource object
        resource = Resource(1, "White Noise", Name("Don", "", "DeLillo"), 
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
        self.assertEqual(str(resource), ("ID: 1 \nTitle: White Noise "\
            "\nCreator: Don DeLillo \nSummary: Delillo's White Noise follows "\
            "narrator Jack Gladney, a professor at a \nsmall Liberal Arts "\
            "college and describes an academic year. Jack teaches \nat ... "\
            "\nGenre: sci-fi \nLanguage: English \nYear: 1985 "\
            "\nCountry: US \nLength: 326p \nType: book "\
            "\nKeywords: culture, life, society, survival"))
            
    def test_repr(self):
        """
        Test that the repr method returns an official representation of the
        object as a string.
        """
        
        # Create a Resource object
        resource = Resource(1, "White Noise", Name("Don", "", "DeLillo"), 
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
        self.assertEqual(repr(resource), ("Resource(1, 'White Noise', "\
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
                            "'['culture', 'survival', 'life', 'society']')"))
    
    def test_get_brief_summary_output(self):
        """ Test get_brief_summary method's output in Resource class"""
        
        # Create a Resource object
        resource = Resource(1, "White Noise", Name("Don", "", "DeLillo"), 
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
        
        # Assert expected results       
        self.assertEqual(resource.get_brief_summary(), "Delillo's White "\
                         "Noise follows narrator Jack Gladney, a professor "\
                         "at a \nsmall Liberal Arts college and describes an "\
                         "academic year. Jack teaches \nat ...")
        
    def test_get_brief_summary_length(self):
        """ Test get_brief_summary method's output length in Resource class""" 
        
        # Create a Resource object
        resource = Resource(1, "White Noise", Name("Don", "", "DeLillo"), 
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
        
        # Assert expected results
        self.assertLessEqual(len(resource.get_brief_summary()), 150) 
        
    def test_get_runtime_in_hours(self):
        """
        Test that get_runtime_in_hours returns the runtime of the movie
        as a tuple that contains the hours in index 0 and the minutes in index 1
        """
        
        # Create a movie object
        resource = Resource(2, "A clockwork Orange", [Name("Stanley", "Kubrick")], 
              "Protagonist Alex DeLarge is an ultraviolent youth in "\
              "futuristic Britain. As with all luck, his eventually runs out "\
              "and he's arrested and convicted of murder and rape. While in "\
              "prison, Alex learns of an experimental program in which "\
              "convicts are programmed to detest violence. If he goes "\
              "through the program, his sentence will be reduced and he will "\
              "be back on the streets sooner than expected. But Alex's "\
              "ordeals are far from over once he hits the mean streets of "\
              "Britain that he had a hand in creating.",
              "sci-fi", "English", 1971, "US", 136, "movie",
              ["dystopia", "violence", "alternate society"])
        
        # Assert expected result
        self.assertEqual(resource.get_runtime_in_hours(), (2, 16))  
        
    def test_get_keyword_string(self):
        """ Test get_keyword_string method in Resource class """
        
        # Create a Resource object
        resource = Resource(1, "White Noise", Name("Don", "", "DeLillo"), 
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
               
        # Assert the expected result
        self.assertEqual(resource.get_keyword_string(),
                         "culture, life, society, survival")
        
if __name__ == "__main__":
    
    unittest.main()