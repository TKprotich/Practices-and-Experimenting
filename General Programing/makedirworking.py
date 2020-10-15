import os
PATH = r'C:\Users\user\Documents\notification\workout'
dirs = ["\walert1", "\walert2", "\walert3", "\walert4", "\walert5", "\walert6", "\walert7"]
def makedir(path):
    try:
        os.mkdir(path)
    except:
        print("Directory/Folder Exists!")
def main():
    PATH = input('Enter the path to the director: ')
    dirs = input('Enter the list of directories to be created: ')
    for i in dirs.split(", "):
        path = PATH + i
        makedir(path)
if __name__ ="__main__":
    main()
