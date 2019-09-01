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
    def test_init(self):
        '''
        test_init test to check whether an object is initialized properly
        '''
        self.assertEqual(self.new_user.username,"username","BeatriceWambui")
        self.assertEqual(self.new_user.password,"password","E*7@wach")

    def test_save_user(self):
        '''
        test_save_password test case to test if the password objectis saved into
        the password list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
        # saving new contact
