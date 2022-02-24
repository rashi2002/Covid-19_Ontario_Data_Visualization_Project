#!/usr/bin/env python
'''
Question1.py
  Author(s): Andrew Linington (1060878), Griffin Davis (1125177), Rashi Mathur (1125349)
  Earlier contributors(s): Andrew Hamilton-Wright
  Project: Data analysis on COVID-19 in Ontario (Iteration 0)
  Date of Last Update: Mar 21st, 2021.

  Functional Summary
      Question1.py gets a PHU from the user and a csv file and scans the csv file, counts the specified fields, and outputs the fields to a csv file

     Commandline Parameters: 3
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
    "Row_ID": 0,
    "Accurate_Episode_Date": 1,
    "Case_Reported_Date": 2,
    "Test_Reported_Date": 3,
    "Specimen_Date": 4,
    "Age_Group": 5,
    "Client_Gender": 6,
    "Case_AcquisitionInfo": 7,
    "Outcome1": 8,
    "Outbreak_Related": 9,
    "Reporting_PHU_ID": 10,
    "Reporting_PHU": 11,
    "Reporting_PHU_Address": 12,
    "Reporting_PHU_City": 13,
    "Reporting_PHU_Postal_Code": 14,
    "Reporting_PHU_Website": 15,
    "Reporting_PHU_Latitude": 16,
    "Reporting_PHU_Longitude": 17
}


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
        print("Usage: Question1.py <<data file>> <<PHU ID>>")

        # we exit with a zero when everything goes well, so we choose
        # a non-zero value for exit in case of an error
        sys.exit(1)
    #assigning values to the command line arguments given
    filename = argv[1] 
    PHU_ID = argv[2]

    # print out the specified index column from our sample data
    try:
        fh = open(filename, encoding="utf-8-sig")
        outf = open("Q1data.csv" ,"w")
        
    #eror checking
    except IOError as err:
        print("Unable to open file '{}' : {}".format(filename, err),
              file=sys.stderr)
        sys.exit(1)

    data_reader = csv.reader(fh)

    
    line_count = 0
    data = []

    for row in data_reader:
        # gets the current ID
        reporting_PHU_ID = row[INDEX_MAP["Reporting_PHU_ID"]]
        if reporting_PHU_ID == PHU_ID:
            # if the ID's match then pull in the data for the rows that we want and store them
            temp = []
            temp.append(row[INDEX_MAP["Accurate_Episode_Date"]])
            temp.append(row[INDEX_MAP["Outcome1"]])
            data.append(temp)
            line_count += 1
    # sort the array
    data.sort()
    #prints how the file is to be formatted
    temp = sys.stdout
    sys.stdout = outf
    print("Date,Status,Count")
    #setting variables we are to use
    i = 0
    current_date = data[0][0]
    resolved_count = 0
    death_count =0
    nresolved_count = 0
    

    while (i < line_count):  
        #while loops the iterates as long as the date is same
      while i < line_count and (current_date == data[i][0]):
        if (data[i][1] == "Fatal"):
          death_count += 1
        elif (data[i][1] == "Resolved"):
          resolved_count += 1
        elif (data[i][1] == "Not Resolved"):
          nresolved_count += 1
        i += 1
        #printing once we have the data for a date
        
      print("{},{},{}".format(current_date, "Resolved", resolved_count))
      print("{},{},{}".format(current_date, "Fatal", death_count))
      print("{},{},{}".format(current_date, "Not Resolved", nresolved_count))
      resolved_count = 0
      death_count =0
      nresolved_count = 0
        

        #changing the date
      if (i < line_count):
          current_date = data[i][0]

    
    
    #
    #   End of Function
    #


##
## Call our main function, passing the system argv as the parameter
##
main(sys.argv)

#
#   End of Script
