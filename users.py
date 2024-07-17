'''
Classes for user information for the social network project
'''
import peewee
# pylint: disable=R0903
# pylint: disable=no-member
# pylint: disable=R1710
from loguru import logger



def add_user(user_id, email, user_name, user_last_name, users_table):
    '''
    Adds a new user to the collection
    '''
    try:
        user_find = users_table.find_one(USER_ID=user_id)
        if user_find:
            logger.info("user_id already exists in the dataset", user_id)
            return False

        users_table.insert(USER_ID=user_id, EMAIL=email, NAME=user_name,
                           LASTNAME=user_last_name)
        return True
    except peewee.IntegrityError as e:
        print(f'Error adding user_id: {user_id}, error: {e}')

def modify_user(user_id, email, user_name, user_last_name, users_table):
    '''
    Modifies an existing user
    '''

    try:
        user_up = users_table.find_one(USER_ID=user_id)
        if user_up:
            users_table.update(
                USER_ID=user_id,
                EMAIL=email,
                NAME=user_name,
                LASTNAME=user_last_name,
                columns=['USER_ID'])
            logger.info(f"User {user_id} updated successfully.")
            return True
        logger.info(f"user_id {user_id} does not exist in the dataset")
        return False
    except ValueError as e:
        logger.info(f"user_id {user_id} does not exist in the dataset. Error: {e}")
    return False

def delete_user(user_id, users_table, status_table):
    '''
    Deletes an existing user
    '''
    try:
        delete = users_table.find_one(USER_ID=user_id)

        if delete is not None:
            users_table.delete(USER_ID=user_id)
            status_table.delete(USER_ID=user_id)
        else:
            raise ValueError

    except ValueError as e:
        logger.error(f'User "{user_id}" could not be found. Error: {e}')
        return False

    logger.info(f'User "{user_id}" has deleted successfully.')
    return True

def search_user(user_id, users_table):
    '''
    Searches for user data
    '''
    try:
        search = users_table.find_one(USER_ID=user_id)
        return search

    except users_table.DoesNotExist:
        logger.info("user_id does not exists in the dataset", user_id)
        # Rejects new status if user_id already exists
        return False
