#!/usr/bin/python3

# Use this code to show data on an API
# from python std library
import csv

# python3 -m pip install np
import numpy as np
# python3 -m pip install matplotlib
import matplotlib

#The Agg allows us to save to png in high quality format
matplotlib.use('Agg')
# sudo apt install python3-tk
import matplotlib.pyplot as plt

def parsecsvdata():
    """returns a list. [0] is LAN and [1] WAN data"""
    summary = [] # list that will contain [(LAN), (WAN)]

    # open csv data
    with open("/home/student/mycode/graphing/2018summary.csv",\
     "r") as downtime:
        # parse csv data with csv.reader
        downdata = csv.reader(downtime, delimiter=",")
        #print(type(downdata))
        for row in downdata:
            # rowdat is a tuple not a list, lists are mutable, rearrangle - tuples cannot (immutable) 
            rowdat = (row[0], row[1], row[2], row[3])
            #print(type(rowdat))
            summary.append(rowdat) # add dict to list
    return summary

def main():
    #number of bars in our graph, we know we have 4 data points in csv file
    N = 4
    ## grab our data
    summary = parsecsvdata() # grab our data
    localnetMeans = summary[0] # LAN data
    wanMeans = summary[1] # WAN data

    ind = np.arange(N)    # the x locations for the groups, creates a set of numbers based on N
    # the width of the bars: can also be len(x) sequence
    width = 0.35

    # describe where to display p1
    p1 = plt.bar(ind, localnetMeans, width)
    # stack p2 on top of p1
    p2 = plt.bar(ind, wanMeans, width, bottom=localnetMeans)

    # Describe the table metadata
    plt.ylabel("Length of Outage (mins)")
    plt.title("2018 Network Summary")
    plt.xticks(ind, ("Q1", "Q2", "Q3", "Q4"))
    plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0]), ("LAN", "WAN"))

    # SAVE the graph
    plt.savefig("/home/student/static/2018summaryv2.png")
    print("Graph created.")

if __name__ == "__main__":
    main()

