'''
classes to manage the user status messages
'''
# pylint: disable=R0903
# pylint: disable=no-member

from loguru import logger
import peewee
def add_status(status_id, user_id, status_text, status_table, users_table):
    '''
    add a new status message to the collection
    '''

    try:
        search = users_table.find_one(USER_ID=user_id)

        if search is not None:
            try:
                status_table.insert(USER_ID=user_id, STATUS_ID=status_id, STATUS_TEXT=status_text)

            except peewee.IntegrityError as e:
                logger.error(f'Status "{status_id}" could not be added to the database.')
                logger.error(e)
                return False
        else:
            raise ValueError

    except ValueError:
        logger.error(f'Status "{status_id}" could not be added '
                     f'because User "{user_id}" does not exist.')
        return False

    return True

def modify_status(status_id, user_id, status_text, status_table):
    '''
    Modifies a status message

    The new user_id and status_text are assigned to the existing message
    '''
    try:
        status_up = status_table.find_one(USER_ID=user_id)
        if status_up:
            status_table.update(
                STATUS_ID=status_id,
                USER_ID=user_id,
                STATUS_TEXT=status_text,
                columns=['STATUS_ID'])
            logger.info("Status updated successfully.", status_id)
            return True

        logger.info("status_id does not exist in the dataset", status_id)
        return False
    except status_table.DoesNotExist:
        logger.info("status_id does not exist in the dataset", status_id)
    return False

def delete_status(status_id, status_table):
    '''
    deletes the status message with id, status_id
    '''
    try:
        search = status_table.find_one(STATUS_ID=status_id)

        if search is not None:
            status_table.delete(STATUS_ID=status_id)
        else:
            raise ValueError
    except ValueError:
        logger.info("status_id does not exists in the dataset", status_id)
        return False
    return True

def search_status(status_id, status_table):
    '''
    Find and return a status message by its status_id

    Returns an empty UserStatus object if status_id does not exist
    '''
    try:
        search = status_table.find_one(STATUS_ID=status_id)
        return search

    except status_table.DoesNotExist:
        logger.info("status_id does not exists in the dataset", status_id)
        return False
