from password import Credentials
from password import User
def create_password(account,first_name,password,cls):
    ''' 
    function to create a new password
    '''
    new_password = Credentials(account,first_name,password,cls) 
    return new_password
def save_password(password):
    '''
    function to create a new password for the user
    '''
    password.save_password()
def delete_password(password):
    '''
    function to delete aa pasword for the user
    '''
    password.delete_password():
def check_existing_password(first_name):
    '''
    function that checks if password exists with that name and returns a Boolean
    '''
    

