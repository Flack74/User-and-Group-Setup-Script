#!/usr/bin/env python3

import subprocess
import os

userlist = ["alpha", "beta", "gamma"]
groupname = "science"
shared_dir = "/opt/science_dir"

def run_command(command, check=False, capture_output=False):
    try:
        return subprocess.run(command, check=check, capture_output=capture_output, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Command '{' '.join(command)}' failed with error: {e}")
        return None

def user_exists(username):
    return run_command(["id", username]).returncode == 0

def group_exists(groupname):
    return run_command(["getent", "group", groupname]).returncode == 0

def add_user(username):
    print(f"User {username} does not exist. Adding...")
    run_command(["useradd", username], check=True)

def add_group(groupname):
    print(f"Group {groupname} does not exist. Adding...")
    run_command(["groupadd", groupname], check=True)

def add_user_to_group(username, groupname):
    print(f"Adding user {username} to group {groupname}...")
    run_command(["usermod", "-aG", groupname, username], check=True)

def create_directory_if_not_exists(path, groupname):
    if not os.path.isdir(path):
        print(f"Creating directory: {path}")
        os.mkdir(path)
    else:
        print(f"Directory {path} already exists. Skipping.")
    
    print("Setting ownership and permissions...")
    run_command(["chown", f":{groupname}", path], check=True)
    run_command(["chmod", "770", path], check=True)

# Main script
print("\n=== Adding Users to System ===")
for user in userlist:
    if not user_exists(user):
        add_user(user)
    else:
        print(f"User {user} already exists. Skipping.")

print("\n=== Group Management ===")
if not group_exists(groupname):
    add_group(groupname)
else:
    print(f"Group '{groupname}' already exists. Skipping.")

print("\n=== Assigning Users to Group ===")
for user in userlist:
    add_user_to_group(user, groupname)

print("\n=== Directory Setup ===")
create_directory_if_not_exists(shared_dir, groupname)

print("\n✅ Setup completed successfully.")
