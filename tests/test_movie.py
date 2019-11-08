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
"""

from Movie import Movie
from Name import Name
import unittest

class TestMovie(unittest.TestCase):
    """ Test methods from Movie class """
    
    def test_str(self):
        """ 
        Test that str method returns a string representation of the object.
        """
        
        # Create a movie object
        movie = Movie("R",[Name("Stanley", "", "Kubrick"), 
                Name("Anthony", "", "Burgess")],
                [Name("Malcolm", "", "McDowell"), Name("Patrick", "", "Magee"), 
                Name("Michael", "", "Bates")], 2, "A clockwork Orange",
                Name("Stanley", "Kubrick"), 
                "Protagonist Alex DeLarge is an ultraviolent youth in "\
                "futuristic Britain. As with all luck, his eventually runs out "\
                "and he's arrested and convicted of murder and rape. While in "\
                "prison, Alex learns of an experimental program in which "\
                "convicts are programmed to detest violence. If he goes "\
                "through the program, his sentence will be reduced and he will "\
                "be back on the streets sooner than expected. But Alex's "\
                "ordeals are far from over once he hits the mean streets of "\
                "Britain that he had a hand in creating.",
                "sci-fi", "English", 1971, "US", 136,  "movie",
                ["dystopia", "violence", "alternate society"])
        
        # Assert expected result of the str function
        self.assertEqual(str(movie), ("ID: 2 \nTitle: A clockwork Orange "\
                "\nCreator: Stanley  \nSummary: Protagonist Alex DeLarge is "\
                "an ultraviolent youth in futuristic Britain. \nAs with all "\
                "luck, his eventually runs out and he's arrested and "\
                "convicted... \nGenre: sci-fi \nLanguage: English "\
                "\nYear: 1971 \nCountry: US \nLength: 2h 16m \nType: movie "\
                "\nKeywords: alternate society, dystopia, violence"\
                "\nRating: R \nWriters: Stanley Kubrick, Anthony Burgess"\
                "\nCast: Malcolm McDowell, Patrick Magee, Michael Bates "))
        
    def test_repr(self):
        """
        Test that the repr method returns an official representation of the
        object as a string.
        """
        
        # Create a movie object
        movie = Movie("R",[Name("Stanley", "", "Kubrick"), 
                Name("Anthony", "", "Burgess")],
                [Name("Malcolm", "", "McDowell"), Name("Patrick", "", "Magee"), 
                Name("Michael", "", "Bates")], 2, "A clockwork Orange",
                Name("Stanley", "Kubrick"), 
                "Protagonist Alex DeLarge is an ultraviolent youth in "\
                "futuristic Britain. As with all luck, his eventually runs out "\
                "and he's arrested and convicted of murder and rape. While in "\
                "prison, Alex learns of an experimental program in which "\
                "convicts are programmed to detest violence. If he goes "\
                "through the program, his sentence will be reduced and he will "\
                "be back on the streets sooner than expected. But Alex's "\
                "ordeals are far from over once he hits the mean streets of "\
                "Britain that he had a hand in creating.",
                "sci-fi", "English", 1971, "US", 136,  "movie",
                ["dystopia", "violence", "alternate society"])
        
        
        # Assert expected result of the repr function
        self.assertEqual(repr(movie), ("Movie(2, 'A clockwork Orange', "\
            "Name('Stanley', 'Kubrick', ''), 'Protagonist Alex DeLarge is an "\
            "ultraviolent youth in futuristic Britain. As with all luck, his "\
            "eventually runs out and he's arrested and convicted of murder "\
            "and rape. While in prison, Alex learns of an experimental "\
            "program in which convicts are programmed to detest violence. "\
            "If he goes through the program, his sentence will be reduced "\
            "and he will be back on the streets sooner than expected. But "\
            "Alex's ordeals are far from over once he hits the mean streets "\
            "of Britain that he had a hand in creating.', 'sci-fi', "\
            "'English', 1971, 'US', 136, 'movie', "\
            "'['dystopia', 'violence', 'alternate society']', "\
            "'R','[Name('Stanley', '', 'Kubrick'), "\
            "Name('Anthony', '', 'Burgess')]', "\
            "'[Name('Malcolm', '', 'McDowell'), Name('Patrick', '', 'Magee'), "\
            "Name('Michael', '', 'Bates')]'"))
    
    def test_get_names_string(self):
        """
        Test that get_names_string returns a string that contains a list of 
        names.
        """
        
        # Create a movie object
        movie = Movie("R",[Name("Stanley", "", "Kubrick"), 
                Name("Anthony", "", "Burgess")],
                [Name("Malcolm", "", "McDowell"), Name("Patrick", "", "Magee"), 
                Name("Michael", "", "Bates")], 2, "A clockwork Orange",
                Name("Stanley", "Kubrick"), 
                "Protagonist Alex DeLarge is an ultraviolent youth in "\
                "futuristic Britain. As with all luck, his eventually runs out "\
                "and he's arrested and convicted of murder and rape. While in "\
                "prison, Alex learns of an experimental program in which "\
                "convicts are programmed to detest violence. If he goes "\
                "through the program, his sentence will be reduced and he will "\
                "be back on the streets sooner than expected. But Alex's "\
                "ordeals are far from over once he hits the mean streets of "\
                "Britain that he had a hand in creating.",
                "sci-fi", "English", 1971, "US", 136,  "movie",
                ["dystopia", "violence", "alternate society"])
        
        # Assert expected result
        self.assertEqual(movie.get_names_string(movie.cast), 
                         "Malcolm McDowell, Patrick Magee, Michael Bates")
        
if __name__ == "__main__":
    
    unittest.main()