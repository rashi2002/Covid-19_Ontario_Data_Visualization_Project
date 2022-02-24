
'''
Question2.py


  Author(s): Rashi Mathur (1125349),Griffin Davis (1125177),Andrew Linington (1060878),Adhyayan Bhandari(1135943)
  Earlier contributors(s): Andrew Hamilton-Wright
  Project: Data analysis on COVID-19 in Ontario (Iteration 0)
  Date of Last Update: Mar 21st, 2021.

  Functional Summary
      Question2.py preprocesses and outputs the data in a sorted manner to to plotted and interpreted

     Commandline Parameters: 4
        argv[0] = script
        argv[1] = data file
        argv[2] = first PHU Id for inquiry
        argv[3] = second PHU Id for inquiry 
'''


# ************Packages and modules*********************#

#**********************************************************#

# The 'sys' module gives us access to system tools, including the command line parameters, as well as standard input, output and error
#The csv module implements classes to read and write tabular data in CSV format.
#**********************************************************#

import sys
import csv

#**********************************************************#
# This is a dictionary -- a data structure that associates values (in this case integers) with names.
#**********************************************************#


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

#*************The main function**********************#

def main(argv):
    '''
    Load a data file and print out the columns matching the selected
    indices
    '''

    #*****************************************************#
    # Check that we have been given the right number of parameters
    #*****************************************************#

    if len(argv) != 4:
        print(
            "Usage: Question2.py <data file>> <PHU_ID1> <PHU_ID2>")
        #*************************************************#
        # we exit with a zero when everything goes well, so we choose a non-zero value for exit in case of an error
        #*************************************************#
        sys.exit(1)
    
    #*****************************************************#
    # Giving better names to the command line arguments 
    #*****************************************************#

    data_filename = argv[1]
    PHU_ID1 = argv[2]
    PHU_ID2 = argv[3]

    #*****************************************************#
    # Trying to open the file. If the file is not successfully opened, it prints out the error message and exits the main with a value of 1
    #*****************************************************#


    try:
        fh = open(data_filename, encoding="utf-8-sig")
        outf = open("Q2data.csv" ,"w")

    except IOError as err:
        print("Unable to open file '{}' : {}".format(data_filename, err),
              file=sys.stderr)
        sys.exit(1)

    #*****************************************************#
    # Reading the CSV filename
    #*****************************************************#

    data_reader = csv.reader(fh)

    #*****************************************************#
    #initialising line_count to count the number of entries from either one of the PHU Ids and initialising data, an array that will contain the required data from the file.
    #*****************************************************#

    line_count = 0
    data = []

    #*****************************************************#
    #begining the loop to read through the file
    #*****************************************************#

    for row in data_reader:

        #*****************************************************#
        # LOGIC USED: Set the pHU ID of the current row to be the reporting_PHU_ID. If it is equal to either one of the phu Ids in inquiry, then append the accurate episode date and the PHU Id to temp which is created to seve as a 1d array which will then be appended to data, the 2d array
        #*****************************************************#
        
        reporting_PHU_ID = row[INDEX_MAP["Reporting_PHU_ID"]]
        if (reporting_PHU_ID == PHU_ID1) or (reporting_PHU_ID == PHU_ID2):
            temp = []
            temp.append(row[INDEX_MAP["Accurate_Episode_Date"]])
            temp.append(row[INDEX_MAP["Reporting_PHU_ID"]])
            data.append(temp)
            line_count = line_count + 1

    #*****************************************************#
    #Sorts the data according to the dates since they are the first entries in the 2d array, data.
    #*****************************************************#

    data.sort()

    #*****************************************************#
    # printing the header and initialising the iterative variable and the current date to the first date in data
    #*****************************************************#
    temp = sys.stdout
    sys.stdout = outf
    print("Date,PHU_Id,Count")
    i = 0
    current_date = data[0][0]

    while (i < line_count):
        #reinitialising the counts for every date
        PHU_ID1_count = 0
        PHU_ID2_count = 0
        #while loops the iterates as long as the date is same
        while i < line_count and (current_date == data[i][0]):
            if (data[i][1] == PHU_ID1):
                PHU_ID1_count += 1
            else:
                PHU_ID2_count += 1
            i += 1
        #printing once we have the data for a date
        print("{},{},{}".format(current_date, PHU_ID1, PHU_ID1_count))
        print("{},{},{}".format(current_date, PHU_ID2, PHU_ID2_count))

        #changing the date
        if (i < line_count):
            current_date = data[i][0]

    
    #***************End of Function******************#
    

#******************************************************#
# Call our main function, passing the system argv as the parameter
#******************************************************#

main(sys.argv)

#*******************End of script**********************#
