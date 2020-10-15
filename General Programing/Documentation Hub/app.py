""" Documentation Hub"""
import time
import datetime as dt
import traceback
#####My appa##
from dailyactionlogs import *
from entertainmenthub import *
from excercisehub import *
from noteshub import *
from studieshub import *
from webscrapinghub import *
class time_manager:
    def __init__(self):
        self.todos = []
    def registertodo(self, todo, start, end):
        self.todo = todo
        self.todos.append("{}, {}, {}".format(todo, start, end))

    # Read todos
    def action(self):
        pass
        


def main():
    try:
        openbrowser()
        sendmessage("Good to go!", "My Messages")
    except:
        print("Internet Problem")
    while True:
        try:
            if input('Do you intend to read? ').lower() == 'yes':
                studytrack()
            elif input('Do you intend to Work? ').lower() == 'yes':
                actionlog()

            elif input('Do you intend to Write a note? ').lower() == 'yes':
                notes()
            elif input('Do you intend to do excercise? ').lower() == 'yes':
                start=time.time()
                excercise()
                stop = time.time()
                print("You finished in {} minutes".format((stop-start)/60))
                entertainment()
            else:
                entertainment()
        except Exception:
            traceback.print_exc()
            main()
if __name__ == "__main__":
 main()
