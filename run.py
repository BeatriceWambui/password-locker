#!/usr/bin/env python3.6
import unittest
import pyperclip
from password import Credentials
from password import User

def create_credentials(account,first_name,password):
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
def find_credentials(first_name):
    '''
    function that finds credentials by password
    '''
    return Credentials.find_by_name(first_name)
def check_existing_credentials(first_name):
    '''
    function that checks if credentials exists with that name and returns a Boolean
    '''
    return Credentials.credentials_exist(first_name)

def main():
    print("This is your credentials.Enter username ")
    user_name = input()
    print(f"Hello {user_name} This is your new credentials")

print('\n')
while True:
    print("Use the following short codes : cc - create a new account,dc - display credentials,fc -find a contact, ex -exit")
    
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

        print("password")
        password=input()
        save_credentials(create_credentials(first_name,account,password)) # create and save new contact.
        print ('\n')
        print(f"New Credentials {first_name} {password} created")
        print ('\n')
   
    elif short_code == "ex":
        # print("Thankyou")
        break
    else:
        print("I really didn't get that. Please use the short codes")




