'''
main driver for a simple social network project
'''
import peewee
from playhouse.dataset import DataSet
import users
import user_status


dataset = DataSet('sqlite:///socialnetwork.db')

def load_users(filename, users_table):
    '''
    Opens a CSV file with user data and
    adds it to an existing instance of
    UserCollection

    Requirements:
    - If a user_id already exists, it
    will ignore it and continue to the
    next.
    - Returns False if there are any errors
    (such as empty fields in the source CSV file)
    - Otherwise, it returns True.
    '''
    try:

        users_table.thaw(filename=filename, format='csv')
        print("Users loaded successfully")
        return True

    except peewee.IntegrityError as e:
        print(f"Error: {e}")
        return False

def load_status_updates(filename, status_table):
    '''
    Opens a CSV file with status data and adds it to an existing
    instance of UserStatusCollection

    Requirements:
    - If a status_id already exists, it will ignore it and continue to
      the next.
    - Returns False if there are any errors(such as empty fields in the
      source CSV file)
    - Otherwise, it returns True.
    '''
    try:
        status_table.thaw(filename=filename, format='csv')
        return True

    except peewee.IntegrityError as e:
        print(f"Error: {e}")
        return False

def add_user(user_id, email, user_name, user_last_name, users_table):
    '''
    Creates a new instance of User and stores it in user_collection
    (which is an instance of UserCollection)

    Requirements:
    - user_id cannot already exist in user_collection.
    - Returns False if there are any errors (for example, if
      user_collection.add_user() returns False).
    - Otherwise, it returns True.
    '''
    user_add = users.add_user(user_id, email, user_name, user_last_name, users_table)

    return user_add

def update_user(user_id, email, user_name, user_last_name, users_table):
    '''
    Updates the values of an existing user

    Requirements:
    - Returns False if there any errors.
    - Otherwise, it returns True.
    '''


    return users.modify_user(user_id, email, user_name, user_last_name, users_table)

def delete_user(user_id, users_table, status_table):
    '''
    Deletes a user from user_collection.

    Requirements:
    - Returns False if there are any errors (such as user_id not found)
    - Otherwise, it returns True.
    '''

    user_delete = users.delete_user(user_id, users_table, status_table)
    return user_delete

def search_user(user_id, users_table):
    '''
    Searches for a user in user_collection(which is an instance of
    UserCollection).

    Requirements:
    - If the user is found, returns the corresponding User instance.
    - Otherwise, it returns None.
    '''
    user_search = users.search_user(user_id, users_table)

    return user_search


def add_status(status_id, user_id, status_text, status_table, users_table):
    '''
    Creates a new instance of UserStatus and stores it in
    user_collection(which is an instance of UserStatusCollection)

    Requirements:
    - status_id cannot already exist in user_collection.
    - Returns False if there are any errors (for example, if
      user_collection.add_status() returns False).
    - Otherwise, it returns True.
    '''
    status_add = user_status.add_status(status_id, user_id, status_text, status_table, users_table)

    return status_add


def update_status(status_id, user_id, status_text, status_table):
    '''
    Updates the values of an existing status_id

    Requirements:
    - Returns False if there any errors.
    - Otherwise, it returns True.
    '''
    modify = user_status.modify_status(status_id, user_id, status_text, status_table)
    return modify


def delete_status(status_id, status_table):
    '''
    Deletes a status_id from user_collection.

    Requirements:
    - Returns False if there are any errors (such as status_id not found)
    - Otherwise, it returns True.
    '''

    status_delete = user_status.delete_status(status_id, status_table)
    return status_delete

def search_status(status_id, status_table):
    '''
    Searches for a status in status_collection

    Requirements:
    - If the status is found, returns the corresponding
    UserStatus instance.
    - Otherwise, it returns None.
    '''
    status_search = user_status.search_status(status_id, status_table)


    return status_search
