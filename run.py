import unittest
import pyperclip
from password import Credentials
from password import User
def create_credentials(account,first_name,cls,password):
    ''' 
    function to create a new credentials
    '''
    new_credentials = Credentials(account,first_name,password) 
    return new_credentials
def save_credentials(credentials):
    '''
    function to create a new credentials for the user
    '''
    credentials.save_credentials()
def delete_credentials(credentials):
    '''
    function to delete a users credentials for the user
    '''
    credentials.delete_credentials()
def find_credentials(password):
    '''
    function that finds credentials by password
    '''
    return Credentials.find_by_password(password)
def check_existing_credentials(first_name):
    '''
    function that checks if credentials exists with that name and returns a Boolean
    '''
    return Credentials.credentials_exist(first_name)
def display_credentials():
    '''
    function that returns all saved credentials
    '''
    return Credentials.display_credentials()

def main():
    print("This is your credentials.Enter username ")
    user_name = input()
    print(f"Hello {user_name} This is your new credentials")

    print('\n')
    while True:
            print("Use the following short codes : cc - create a new account,dc - display credentials,fc -find a contact, ex -exit the contact list")
            
            short_code = input().lower()

            if short_code == 'cc':
                print("New Credentials")
                print("-"*10)

                print("First name ")
                first_name = input()

                print("credentials")
                credentials = input()

                print("account")
                account = input()
                save_credentials(create_credentials(first_name,account,password)) # create and save new contact.
                print ('\n')
                print(f"New Credentials {first_name} {password} created")
                print ('\n')
            elif short_code == 'dc':

                            if display_credentials():
                                    print("Here is a list of all your accounts")
                                    print('\n')

                                    for credentials in display_credentials():
                                            print(f"{credentials.first_name} {credentials.password} .....{credentials.account}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any credentials saved yet")
                                    print('\n')

            elif short_code == 'fc':

                            print("Enter the password you want to search for")

                            search_password = input()
                            if check_existing_credentials(search_password):
                                    search_password = find_password(search_password)
                                    print(f"{search_credentials.first_name} {search_credentials.account}")
                                    print('-' * 20)

                                    print(f"first_name.......{search_credentials.first_name}")
                                    print(f"password.......{search_password}")
                            else:
                                    print("That  does not exist")

            elif short_code == "ex":
                            print("Thankyou")
                            break
            else:
                            print("I really didn't get that. Please use the short codes")




