"""
Script to delete environments created.
Author: Keegan Donley
"""
import os
import urllib
import shutil

# The colors used for highlighting text output
class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    LOG = '\033[90m'
    ENDC = '\033[0m'


def main():
    print_welcome()
    folderlocation = 'Documents'
    rootdir = get_root_dir()

    # Set the working directory to /Users/<username>/Documents
    # Only works currently if the script is run from a folder located below /Users/<username>/
    while rootdir != os.getcwd():
        os.chdir(os.pardir)
        rootdir = get_root_dir()
    os.chdir(folderlocation)

    repeat_confirm = "Y"
    while repeat_confirm.upper() == "Y":
        print(os.getcwd())
        # Confirm that the directory entered is valid
        folder_to_delete = get_folder_to_delete(folderlocation)
        confirmation = confirm_delete(folder_to_delete)
        if confirmation:
            print(colors.OKGREEN + "Deleted folder " + folder_to_delete + colors.ENDC)
            shutil.rmtree(folder_to_delete)
        repeat_confirm = raw_input("Would you like to delete another? (Y/N): ")
        while repeat_confirm.upper() != "Y" and repeat_confirm.upper() != "N":
            os.system('clear')
            print("Please enter either 'Y' or 'N'")
            repeat_confirm = raw_input("Would you like to delete another? (Y/N): ")
        os.system('clear')

def confirm_delete(folder):
    os.system('clear')
    print("Current Directory: " + os.getcwd() + "\n")
    print(colors.FAIL + "--------------------------------------------------------" + colors.ENDC)
    print(colors.FAIL + "WARNING! You're about to permanently delete " + folder + "." + colors.ENDC)
    print(colors.FAIL + "--------------------------------------------------------\n" + colors.ENDC)
    confirmation = raw_input("Are you sure you'd like to do this? (Y/N): ")
    while confirmation.upper() != "Y" and confirmation.upper() != "N":
        os.system('clear')
        print("Current Directory: " + os.getcwd() + "\n")
        print(colors.FAIL + "\n--------------------------------------------------------" + colors.ENDC)
        print(colors.FAIL + "WARNING! You're about to permanently delete " + folder + "." + colors.ENDC)
        print(colors.FAIL + "--------------------------------------------------------\n" + colors.ENDC)
        print("Please enter either 'Y' or 'N'")
        confirmation = raw_input("Are you sure you'd like to do this? (Y/N): ")
    if confirmation.upper() == "Y":
        return True
    elif confirmation.upper() == "N":
        return False

def get_folder_to_delete(folderlocation):
    folder = raw_input("Please enter the name of the project you'd like to delete (case-sensitive): ")
    folder_path = os.getcwd() + "/" + folder + "/"
    while os.path.isdir(folder_path) == False:
        print(colors.FAIL + "!! Directory doesn't exist! !!" + colors.ENDC)
        folder = raw_input("Please enter the name of the project you'd like to delete (case-sensitive): ")
        folder_path = "/" + folder + "/"
    folder_path = folder_path.split('/')
    return folder_path[-2]


def get_root_dir():
    '''
    This function determines the root directory to change the working directory to.
    returns: string of the root directory, in the format /Users/<username>/
    '''
    currentdir = os.getcwd()
    currentdir = currentdir.split('/')
    rootdir = '/' + currentdir[1] + '/' + currentdir[2]
    return rootdir


def print_welcome():
    '''
    Print the welcome screen for the user.
    '''
    os.system('clear')
    print(colors.OKBLUE + "------------- Web Heirarchy Deleter ------------")
    print("By Keegan Donley\n")
    print("Please begin by entering the desired name of your")
    print("site you'd like to delete\n")
    print(colors.FAIL + "WARNING: This script deletes files from your system. Use carefully")
    print("at your own risk!")
    print(colors.OKBLUE + "--------------------------------------------------\n" + colors.ENDC)

main()
