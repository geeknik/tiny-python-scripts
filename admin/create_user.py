
import os
import subprocess

def create_user(username, password):
    try:
        # Create a new user
        subprocess.run(['useradd', '-m', username], check=True)

        # Set the user's password
        subprocess.run(['echo', f'{username}:{password}', '|', 'chpasswd'], check=True)

        print(f'User {username} created successfully.')
    except subprocess.CalledProcessError:
        print(f'Failed to create user {username}.')

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: create_user.py <username> <password>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]

    create_user(username, password)
