
import os
import sys
import subprocess

def modify_user(username, new_data):
    try:
        command = "usermod"
        args = []

        if 'password' in new_data:
            args += ['-p', new_data['password']]
        if 'home' in new_data:
            args += ['-d', new_data['home']]
        if 'shell' in new_data:
            args += ['-s', new_data['shell']]
        if 'comment' in new_data:
            args += ['-c', new_data['comment']]

        args.append(username)

        subprocess.run([command] + args, check=True)
        print(f"User {username} modified successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to modify user {username}.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: modify_user.py <username> <new_data>")
        sys.exit(1)

    username = sys.argv[1]
    new_data = eval(sys.argv[2])

    modify_user(username, new_data)
