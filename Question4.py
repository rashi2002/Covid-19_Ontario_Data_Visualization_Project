#!/usr/bin/env python

'''
  Author(s): Andrew Linington (1060878), Griffin Davis (1125177), Rashi Mathur (1125349), Adhyayan Bhandari(1135943)
  Earlier contributors(s): Andrew Hamilton-Wright
  Project: Data analysis on COVID-19 in Ontario
  Date of Last Update: Mar 21st, 2021.
python Question_4/Q4_prototype.py conposcovidloc.csv 2236 > Q4Data2.csv
Functional Summary
      Question4.py takes command line arguments of data file and PHU ID and splits the data into specified age groups. It then prints the files to a csv file to be used to create a plot

     Commandline Parameters: 1
        argv[0] = data file
        argv[1] = csv file
        argv[2] = PHU ID
'''


#
#   Packages and modules
#

# The 'sys' module gives us access to system tools, including the
# command line parameters, as well as standard input, output and error
import sys

# command line parameters, as well as standard input, output and error
import csv


#
# Define any "constants" for the file here.
# Names of constants should be in UPPER_CASE.
#
# This is a dictionary -- a data structure that associates
# values (in this case integers) with names.
INDEX_MAP = {
        "Row_ID" :  0,
        "Accurate_Episode_Date" :  1,
        "Case_Reported_Date" :  2,
        "Test_Reported_Date" :  3,
        "Specimen_Date" :  4,
        "Age_Group" :  5,
        "Client_Gender" :  6,
        "Case_AcquisitionInfo" :  7,
        "Outcome1" :  8,
        "Outbreak_Related" :  9,
        "Reporting_PHU_ID" : 10,
        "Reporting_PHU" : 11,
        "Reporting_PHU_Address" : 12,
        "Reporting_PHU_City" : 13,
        "Reporting_PHU_Postal_Code" : 14,
        "Reporting_PHU_Website" : 15,
        "Reporting_PHU_Latitude" : 16,
        "Reporting_PHU_Longitude" : 17 }
  

def main(argv):
    '''
    Load a data file and print out the columns matching the selected
    indices
    '''
    #
    #   Check that we have been given the right number of parameters,
    #   and store the single command line argument in a variable with
    #   a better name
    #
    if len(argv) != 3:
        print("Usage: Q1_prototype.py <data file>> <PHU ID>> > <<csv file>>")

        # we exit with a zero when everything goes well, so we choose
        # a non-zero value for exit in case of an error
        sys.exit(1)
    #setting variables from command line
    filename = argv[1]
    PHU_ID = argv[2]


    # print out the specified index column from our sample data
    try:
        fh = open(filename, encoding="utf-8-sig")
        outf = open("Q4data.csv" ,"w")
    #error checking
    except IOError as err:
        print("Unable to open file '{}' : {}".format(
                filename, err), file=sys.stderr)
        sys.exit(1)

    data_reader = csv.reader(fh)

    
    line_count = 0
    data = []
    
   
    for row in data_reader:
      # gets the current ID
      reporting_PHU_ID = row[ INDEX_MAP["Reporting_PHU_ID"] ]
      if reporting_PHU_ID == PHU_ID:
        # if the ID's match then pull in the data for the row and store them
        temp = []
        temp.append(row[ INDEX_MAP["Age_Group"]])
        data.append(temp)
        line_count += 1
    # sort the array
    data.sort()
    #set variables for the loops
    i = 0
    #print how the results will be outputted
    temp = sys.stdout
    sys.stdout = outf
    print("Age group,Count")
    group1_count = 0
    group2_count = 0
    group3_count = 0
    group4_count = 0
    group5_count = 0
    group6_count = 0
    group7_count = 0
    group8_count = 0
    group9_count = 0
    

    while (i < line_count):  
        #while loops the iterates as long as the file is not over
      if (data[i][0] == "<20"):
        group1_count += 1
      elif (data[i][0] == "20s"):
        group2_count += 1
      elif (data[i][0] == "30s"):
        group3_count += 1
      elif (data[i][0] == "40s"):
        group4_count += 1
      elif (data[i][0] == "50s"):
        group5_count += 1
      elif (data[i][0] == "60s"):
        group6_count += 1
      elif (data[i][0] == "70s"):
        group7_count += 1
      elif (data[i][0] == "80s"):
        group8_count += 1
      elif (data[i][0] == "90+"):
        group9_count += 1
      i += 1
            
    #printing once we have the data for a PHU
      
    print("{},{}".format("<20", group1_count))
    print("{},{}".format("20s", group2_count))
    print("{},{}".format("30s", group3_count))
    print("{},{}".format("40s", group4_count))
    print("{},{}".format("50s", group5_count))
    print("{},{}".format("60s", group6_count))
    print("{},{}".format("70s", group7_count))
    print("{},{}".format("80s", group8_count))
    print("{},{}".format("90+", group9_count))
        
    #
    #   End of Function
    #


##
## Call our main function, passing the system argv as the parameter
##
main(sys.argv)


#
#   End of Script
#
