
import os
import sys

def delete_user(username):
    try:
        result = os.system(f'userdel {username}')
        if result == 0:
            print(f'User {username} has been deleted successfully.')
        else:
            print(f'Failed to delete user {username}.')
    except Exception as e:
        print(f'An error occurred: {str(e)}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python delete_user.py <username>')
        sys.exit(1)

    username = sys.argv[1]
    delete_user(username)
