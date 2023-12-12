import unittest
import naughty_pup
from naughty_pup import ThenTheyreGoingToEatMe
from naughty_pup import TheyreEatingHer

class TestNaughtPup(unittest.TestCase):
    def test_check_replace(self):
        text = """Returns a copy of the string `text` with the substring 'goblin' replaced with 'elf' and the substring 'hobgoblin' replaced with 'orc'."""
        response = naughty_pup.troll_check(text)
        # print(response)
        equal = """Returns a copy of the string `text` with the substring 'elf' replaced with 'elf' and the substring 'hobelf' replaced with 'orc'."""
            
        # print(equal)
        self.assertEqual(equal,response, 'goblin and hobgoblin should have been replaced')
    
    
    def test_check_raise(self):
        text = """Returns a copy of the string `text` with the substring 'goblin' replaced with 'elf' and the substring 'hobgoblin' replaced with 'orc'.
        
        Raises `TheyreEatingHer` if the substring 'troll' is found in `text`.
        Raises `ThenTheyreGoingToEatMe` if the substring 'Nilbog' is found in `text`, and the substring 'troll' is not found in `text`."""
        try:
            response = naughty_pup.troll_check(text)
            self.fail("should have raised TheyreEatingHer")
        except Exception as e:
            self.assertIsInstance(e,TheyreEatingHer,'should have raised TheyreEatingHer')
            
    def test_check_nilbog(self):
        text = """Returns a copy of the string `text` with the substring 'goblin' replaced with 'elf' and the substring 'hobgoblin' replaced with 'orc'.
        
        Raises `ThenTheyreGoingToEatMe` if the substring 'Nilbog' is found """
        try:
            response = naughty_pup.troll_check(text)
            self.fail("should have raised TheyreGoingToEatMe")
        except Exception as e:
            self.assertIsInstance(e,ThenTheyreGoingToEatMe,'should have raised ThenTheyreGoingToEatMe')
            
    def test_naughty_checked(self):
        filename ="/home/oni/Downloads/flexistore/Question 3/test.txt"
        self.assertEqual(naughty_pup.print_troll_checked(filename),0,'Should have returned 0')
        filename ="/home/oni/Downloads/flexistore/Question 3/test_1.txt"
        print(filename)
        self.assertEqual(naughty_pup.print_troll_checked(filename),1,"Should have returned 1")
        filename ="/home/oni/Downloads/flexistore/Question 3/test_2.txt"
        self.assertEqual(naughty_pup.print_troll_checked(filename),-1,'Should have returned -1')

    # def test_scan_directory(self):
    #     trolls = naughty_pup.scan_directory("/home/oni/Downloads/flexistore/Question 3",".txt",True)
    #     print(trolls)
    #     self.assertEqual(trolls,1 ,"total files must be 1 with")

if __name__ == '__main__':
    unittest.main()
