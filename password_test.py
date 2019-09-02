import unittest # Importing the unittest module
from password import Credentials # Importing the credentials class
from password import User # importing the user class
###########################

class TestClass(unittest.TestCase):
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
        self.assertEqual(self.new_user.username,"BeatriceWambui")
        self.assertEqual(self.new_user.password,"E*7@wach")
    def test_save_user(self):
        '''
        test_save_password test case to test if the password objectis saved into
        the password list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
        # saving new contact
    def tearDown(self):
        '''
        clean up after every test
        '''
        User.user_list = []
        Credentials.credentials_list = []
    def test_save_multiple_users(self):
        '''
        check whether you can store more than one usere
        '''
        self.new_user.save_user()
        test_user = User("test","password")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
    def test_find_user(self):
        '''
        find a user using username
        '''
        self.new_user.save_user()
        test_user = User("test","password")
        test_user.save_user()
        for user in User.user_list:
            if user.username == test_user.username and user.password == test_user.password:

                found_user = user.username
                return found_user
        self.assertEqual(found_user.username,'test')
    def test_delete_user(self):
        '''
        check whether the user can delete their accounts
        '''
        self.new_user.save_user()
        test_user = User("test","password")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)

class TestCredentials(unittest.TestCase):
    '''
    A test class that defines test cases for credentials class
    '''
    def setUp(self):
        '''
        Method that runs before each individual credentials class
        '''
        self.new_credentials = Credentials('Gmail','BeatriceWambui','E*7@wach')
    def test_init(self):
        '''
        Test case to check if a new Credentials instances has been initialized
        correctly
        '''
        self.assertEqual(self.new_credentials.account,'Gmail')
        self.assertEqual(self.new_credentials.first_name,'BeatriceWambui')
        self.assertEqual(self.new_credentials.password,'E*7@wach')
    def test_save_credentials(self):
        '''
        test case to test if the credentials object is saved into the credentials list.
        '''
        self.new_credentials.save_credentials()
        gmail = Credentials('Gmail','BeatriceWambui','E*7@wach')
        gmail.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)
    def tearDown(self):
        '''
        method that does clean up after each test case has run.
        '''
        Credentials.credentials_list=[]

    def test_delete_credentials(self):
        '''
        test method to test if we can remove an account credentials from our credentials_list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Facebook","beatricewambui","gladweleva")
        test_credentials.save_credentials()
        test_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
   
if __name__ == '__main__':
    unittest.main()
