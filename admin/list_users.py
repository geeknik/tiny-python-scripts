
import os
import pwd

def list_users():
    users = pwd.getpwall()
    for user in users:
        print(f'Username: {user.pw_name}, User ID: {user.pw_uid}, Group ID: {user.pw_gid}, Home: {user.pw_dir}')

if __name__ == "__main__":
    list_users()
