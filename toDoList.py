# Description: Build a to-do list manager application that allows users to create, update, and delete tasks. The application should
# support features like categorizing tasks, setting deadlines, marking tasks as complete, and searching/filtering tasks.
# Skills practiced: Object-oriented programming (OOP), file I/O, data manipulation, user input validation, basic CRUD operations.

# Bonus features:
# Reminders: Implement reminders for upcoming deadlines or tasks.
# User authentication: Add user authentication to allow multiple users to have their own to-do lists.
# Priority levels: Allow users to assign priority levels to tasks and sort/filter tasks based on priority.
# These projects offer a good balance of complexity and learning opportunities, allowing you to apply various Python concepts and 
# libraries while building useful applications. Feel free to start with one project and gradually move to the other as you gain
# confidence and proficiency in Python programming.

import os

def select_user():
    print('Welcome to your to do list manager! Are you a new or existing user?')
    user_selection = input('1: New \n2: Existing \nSelect (1 or 2): ').lower()
    if user_selection not in ('1', '2'): #Make sure the user selected a valid option
        print('\nInvalid selection, please try again.\n')
        return select_user()

    #Print a confirmation message for options 1 & 2 
    confirmation_message = {
        '1': 'You have selected new user. Do you want to go back? (y/n)',
        '2': 'You have selected existing user. Do you want to go back? (y/n)'
    }

    confirmation = input(confirmation_message[user_selection]).lower()
    if confirmation == 'y':
        print ('\nTaking you back...\n')
        return select_user()
    else:
        print('Lets continue!')

    if user_selection == '1': #Create a new user
        while True:
            create_user = input ('Create username: ')
            if os.path.exists(create_user + '_to-do-list'):
                print('That username is already taken. Please choose a different username.')
                continue
            else:
                with open(create_user + '_to-do-list', 'w') as open_to_do_list:
                    print('User & to do list created successfully!')
                break
    elif user_selection == '2': #Log into the existing user
        while True:
            existing_user = input ('What user do you wish to log into? ')
            if not os.path.exists(existing_user + '_to-do-list'):
                print('That user does not exist. Please try again.')
                continue
            else:
                with open(existing_user + '_to-do-list') as open_to_do_list:
                    break

select_user()

def categorize_tasks():
    print ('This is the function that will let users sort their different tasks into categories')
    #For example: Sports, School, Coding, Homework/AfterSchool

def createTask():
    print ('Function to create tasks')
    #In this function, include a feature that asks how important is each task. There will be three levels:
    #Urgent: Tasks that need immediate attention or must be done as soon as possible.
    #Priority: Tasks that are important but not urgent, requiring attention in the near future.
    #Casual: Tasks that are less urgent or can be done at leisure when there is ample time available.

def deleteTask():
    print ('Function to remove tasks')

def modify_task():
    print ('Function to modify tasks')

def markCompleted():
    print ('Lets users mark their tasks as completed')