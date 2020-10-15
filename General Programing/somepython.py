import datetime
import random
import time
import traceback
def revList2(lst):

    def revListHelper(index):
        if index == len(lst):
            return []
        
        result =  revListHelper(index+1) + [lst[index]]
        return result

    return revListHelper(0)

def main():
    #write an XML file with the results
    file = open("ListAccessTiming.xml", "w")

    file.write('<?xml version= "1.0" encoding = "UTF-8" standalone = "no" ?>\n')

    file.write('<plot title = "Average List processing Speed">\n')
    # Record the list size in xList and processing time in yList
    file.write('<Sequence title="Average List processing Speed vs Length" color="red">\n')
    for xmin in list(range(100, 5000, 100)):
        time.sleep(1)
        starttime = time.time()
        xList = []
        print(xList)
        print("Start time:  {}".format(starttime))
        print("Processing........................")
        xList = revList2(list(range(xmin, xmin*200, 1000)))
        print("Completed.........................")
        endtime = time.time()
        print("End time:  {}".format(endtime))
        print("Length of list: {}".format(len(xList)))
        deltaT = endtime - starttime
        accessTime = deltaT*1000
        print("time taken = {} ".format(accessTime))
        file.write(' <DataPoint x="'+str(accessTime)+'" y="'+str(len(xList))+'"/>\n')
  
    file.write(' </Plot>\n')
    file.write(' </Sequence>\n')
    file.close()
if __name__ =="__main__":
    main()
