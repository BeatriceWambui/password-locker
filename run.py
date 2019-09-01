from password import Credentials
from password import User
def create_credentials(account,first_name,password,cls):
    ''' 
    function to create a new credential
    '''
    new_credentials = Credentials(account,first_name,password,cls) 
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
    return Credentials.password_exist(first_name)
def display_password():
    '''
    function that returns all saved passwords
    '''
    return Credential.display_passwords()

def main():
    print("This is your password.Enter username ")
    user_name = input()
    print(f"Hello {user_name} This is your new password")

    print('\n')
        while True:
            print("Use the following short codes : cc - create a new account,dc - display password,fc -find a contact, ex -exit the contact list")
            
            shorl_code = input().lower()

            if short_code == 'cc':
                print("New Credentials")
                print("-"*10)

                print("First name ")
                first_name = input()

                print("Password")
                password = input()

                print("account")
                account = input()
    save_password(create_password(first_name,account,passord)) # create and save new contact.
                            print ('\n')
                            print(f"New Credentials {first_name} {passord} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_password():
                                    print("Here is a list of all your accounts")
                                    print('\n')

                                    for password in display_passwords():
                                            print(f"{password.first_name} {password.password} .....{contact.phone_number}")

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




