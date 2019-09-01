from credentials import Credentials
from credentials import User
def create_credentials(account,first_name,credentials,cls):
    ''' 
    function to create a new credential
    '''
    new_credentials = Credentials(account,first_name,credentials,cls) 
    return new_credentials
def save_credentials(credentials):
    '''
    function to create a new credentials for the user
    '''
    credentials.save_credentials()
def delete_credentials(credentials):
    '''
    function to delete aa pasword for the user
    '''
    credentials.delete_credentials():
def check_existing_credentials(first_name):
    '''
    function that checks if credentials exists with that name and returns a Boolean
    '''
    return Credentials.credentials_exist(first_name)
def display_credentials():
    '''
    function that returns all saved credentialss
    '''
    return Credential.display_credentialss()

def main():
    print("This is your credentials.Enter username ")
    user_name = input()
    print(f"Hello {user_name} This is your new credentials")

    print('\n')
        while True:
            print("Use the following short codes : cc - create a new account,dc - display credentials,fc -find a contact, ex -exit the contact list")
            
            shorl_code = input().lower()

            if short_code == 'cc':
                print("New Credentials")
                print("-"*10)

                print("First name ")
                first_name = input()

                print("credentials")
                credentials = input()

                print("account")
                account = input()
    save_credentials(create_credentials(first_name,account,passord)) # create and save new contact.
                            print ('\n')
                            print(f"New Credentials {first_name} {passord} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_credentials():
                                    print("Here is a list of all your accounts")
                                    print('\n')

                                    for credentials in display_credentialss():
                                            print(f"{credentials.first_name} {credentials.credentials} .....{contact.phone_number}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any contacts saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the number you want to search for")

                            search_number = input()
                            if check_existing_contacts(search_number):
                                    search_contact = find_contact(search_number)
                                    print(f"{search_contact.first_name} {search_contact.last_name}")
                                    print('-' * 20)

                                    print(f"Phone number.......{search_contact.phone_number}")
                                    print(f"Email address.......{search_contact.email}")
                            else:
                                    print("That contact does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")




