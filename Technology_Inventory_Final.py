# Technology inventory: this program manages technolgy device data for a 
# small- midsize company or educational institution.

import technology_class
import pickle

#Global constants for menu choice
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

#Constant for file name
FILENAME = 'technology.dat'

#main function
def main():
    #Load the existing device details dictionary
    #assign it to tech_details
    tech_details = load_technology_details()   #tech = tech devices

    # initialize a variable for the user's choice
    #to control the loop
    choice = 0      

    #Process menu selections until the user
    #wants to quit the program
    while choice != QUIT:
        choice = menu_choice()

        #process the choice
        if choice == LOOK_UP:
            look_up(tech_details)
        elif choice == ADD:
            add(tech_details)
        elif choice == CHANGE:
            change(tech_details)
        elif choice == DELETE:

            delete(tech_details)
        else:
            print('Program Quit')

    #saving the program dictionary to a file
    save_program(tech_details)

def load_technology_details():
    #open device file technology.dat 
    try:
        input_file = open(FILENAME,'rb')

        #unpickle the dictionary
        tech_file = pickle.load(input_file)

        #close the technology.dat file
        input_file.close()

    except IOError:
        #could not open the file, so create
        #an empty dictionary
        tech_file = {}

    #return dictionary
    return tech_file

# the get_menu_choice function displays the menu
# and gets a validated choice from the user.
def menu_choice():
    print()
    print('---------')
    print('-------------')
    print('------------------')
    print('-----------------------')
    print('\tTECHNOLOGY INVENTORY')
    print('*')
    print('**')
    print('***')
    print('****')
    print('*****')
    print('******')
    print('\tPLEASE CHOOSE FROM THE MENU BELOW')
    print()
    print('\tMENU CHOICE')
    print('----------------------------')
    print('----------------------------')
    print('1. Look up an existing device')
    print('2. Add a new device')
    print('3. Update existing device')
    print('4. Delete existing device')
    print('5. Quit the program')
    print('----------------------------')
    print()

    #Get user's choice to make a selection
    user_choice = int(input('Enter choice: '))

    #validate user choice
    while user_choice < LOOK_UP or user_choice > QUIT:
        user_choice = int(input('Invalid choice,Enter a valid choice: '))

    #return user choice
    return user_choice

# the look_up function looks up an item in the
# specified dictionary.
def look_up(details):
    #This will use the serial number as the key,
    #get device's serial_number to look it up
    serial_number = input('Enter Device Serial Number: ')

    #look it up in the dictionary
    print(details.get(serial_number, 'That Serial Number is not found.'))

# the add function adds a new entry into the 
# specified dictionary.
def add(details):
    #get device's info
    item = input('Enter the item: ')
    serial_number = input('Enter the serial number: ')
    needs_servicing = input('Does this device need servicing (Yes/No?): ')
    room_location = input('What room is this device located in: ')

    #create obect named entry
    entry = technology_class.Technology(item,serial_number,needs_servicing,room_location)

    #If the Serial Number does not exist in the dictionary,
    #add it as key with the entry objects as the value
    if serial_number not in details:
        details[serial_number] = entry

        print('The entry has been added.')
    else:
        print('That serial number already exists.')

# the change function changes an existing
# entry in the specified dictionary.
def change(details):
    #get serial number
    serial_number = input('Enter serial number: ')

    #if serial_number is in dictionary,
    #provide new details
    if serial_number in details:
        #get a new name
        item = input('Enter the new item: ')
        #get a needs servicing
        needs_servicing = input('Does this device need servicing? ')
        #get new room location
        room_location = input('Enter new room location: ')

        #create technology object
        entry = technology_class.Technology(item,serial_number,needs_servicing,room_location)

        #updating the entry
        details[serial_number] = entry
        print('information updated.')
    else:
        print('ID Number not found')

# the delete function deletes an entry from the 
# specified dictionary.
def delete(details):
    #get serial number
    serial_number = input('Enter serial number: ')

    #if serial number is in dictionary, delete it
    if serial_number in details:
        del details[serial_number]
        print('Entry deleted.')
    else:
        print('serial number not found.')

# the save_program function pickles the specified
# object and saves it to the technology file.
def save_program(details):
    #open the file for writing
    output_file = open(FILENAME,'wb')

    #pickle the dictionary and save it
    pickle.dump(details, output_file)

    #close the file
    output_file.close()

main()