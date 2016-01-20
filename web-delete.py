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
    projectname = raw_input("Enter your project name: ")
    while len(projectname) <= 0:
        print(colors.FAIL + "Please enter a valid project name!" + colors.ENDC)
        projectname = raw_input("Enter your project name: ")
    folderlocation = 'Documents'
    rootdir = get_root_dir()

    # Set the working directory to /Users/<username>/Documents
    # Only works currently if the script is run from a folder located below /Users/<username>/
    while rootdir != os.getcwd():
        os.chdir(os.pardir)
        rootdir = get_root_dir()
    os.chdir(folderlocation)


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
    print("site you'd like to delete")
    print("--------------------------------------------------\n" + colors.ENDC)

main()
