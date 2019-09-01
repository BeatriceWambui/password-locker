import unittest # importing the unittest module
import pyperclip
class Credentials:
    '''
    This is a class that generates new instances of passwords
    '''

    def __init__ (self,first_name,last_name,password):
        #docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.password = password

        #__init__ nmethod that helps us define propreties for our objects.

        credentials_list = [] # Empty array of password list

        def save_credentials(self):
            '''
            save_password method saves password objects into password_list
            '''

            credentials.credentials_list.append(self)

        def delete_credentials(self):
            '''
            delete_credentials method deletes a saved password from the password_list
            '''

            Credentials.credentials_list.remove(self)

        @classmethod
        def find_by_name(cls,first_name):
            '''
            Method that takes in a name and returns a contact that matches that
            Args:
                name: first name to search for
                returns: Password of person that matches the name.
                '''
                for credentials in cls.credentials_list:
                    if credentials.first_name ==first_name:
                        return credentials

        @classmethod
        def credentials_exist(cls,first_name):
            '''
            Method that checks if a password account exists from the password list.
            Args:
            name: Furst na,e to search if it exists
            Returns:
            Boolean: True or false depending on if the password account exists
            '''
            for credentials in cls.credentials_list:
                if credentials.first_name == first_name:
                    return True
            return False

        @classmethod
        def copy_password(cls,password):
            credentials_found = Credentials.find_by_password(password)
            pyperclip.copy(password_found.password)



if __name__ == '__main__':
    unittest.main() # provides a command line interface that collects all the tests methods and executes them
