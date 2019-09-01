import unittest # Importing the unittest module
 from password import Credentials # Importing the credentials class
 from password import User # importing the user class
###########################

class TestPassword(unittest.TestCase):
    '''
    Test class that defines test cases for the password class behaviors.
    Args:
        unittest.TestCase: TestCase class that helps in creating test credentials_exist
    '''

    def setUp(self):
        '''
        setUp method to run before each test case.
        '''
        self.new_user = User('BeatriceWambui','E*7@wach')
    # def test_init(self):
    #     '''
    #     test
