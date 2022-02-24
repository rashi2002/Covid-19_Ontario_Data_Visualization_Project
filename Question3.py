#!/usr/bin/env python

'''
Question3.py
  Author(s): Andrew Linington (1060878), Griffin Davis (1125177), Rashi Mathur (1125349), Adhyayan Bhandari (1135943)
  Earlier contributors(s): Andrew Hamilton-Wright
  Project: Question 3 script (Final Iteration)
  Date of Last Update: Mar 27th, 2021.

  Functional Summary
      Question3.py creates the preprocessed files for question 3 
      "How does the rate of infection change wghen compared with the rate of vaccination?"
     Commandline Parameters: 1
        Arg[1] = <data infection file> 
        Arg[2] = <data vaccination file>
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
VACCINATION_MAP = {
        "report_date": 0, 
        "previous_day_doses_administered": 1, 
        "total_doses_administered": 2, 
        "total_doses_in_fully_vaccinated_individuals": 3,
        "total_individuals_fully_vaccinated": 4 
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
        print("Usage: Question3.py <data infection file> <data vaccination file>")

        # we exit with a zero when everything goes well, so we choose
        # a non-zero value for exit in case of an error
        sys.exit(1)

    infections_filename = argv[1]
    vaccinations_filename = argv[2]


    # open the files for writing to and for reading from
    try:
        ifh = open(infections_filename, encoding="utf-8-sig")
        vfh = open(vaccinations_filename, encoding="utf-8-sig")
        outf = open("Q3data.csv" ,"w")

    except IOError as err:
        print("Unable to open file '{}' : {}".format(
                infections_filename, err), file=sys.stderr)
        sys.exit(1)

    infections_data_reader = csv.reader(ifh)
    vaccinations_data_reader = csv.reader(vfh)
    start = 0
    data = []
   
    for row in infections_data_reader:
      # creates a composed data set of the most important infection fields
      if start == 0:
        start = 1
      else:
        temp = []
        temp.append(row[ INDEX_MAP["Accurate_Episode_Date"] ])
        temp.append("infection")
        temp.append("1")
        data.append(temp)
    for row in vaccinations_data_reader:
      # creates a composed data set of important vaccination fields
      if start == 1:
        start = 2
      else:
        temp = []
        temp.append(row[ VACCINATION_MAP["report_date"] ])
        temp.append("vaccination")
        numeric = row[ VACCINATION_MAP["total_individuals_fully_vaccinated"] ].replace(",","").replace(" ", "0")
        if numeric == "":
          numeric = "0"
        temp.append(int(numeric))
        data.append(temp)

    # sort the array
    data.sort()
    count = 0
    date_of = data[0][0]
    prev_type = "infection"
    prev_day_total = 0
    # set output to be piped to a file
    temp = sys.stdout
    sys.stdout = outf
    print("Date,Type,Count")
    for d in data:
      #collect total occurances on a date for infections
      if date_of == d[0] and d[1] == "infection":
        count += 1
      elif prev_type == "infection" :
        #print total infections
        print("{},{},{}".format(date_of,"infection",count))
        count = 0
        if d[1] == "vaccination":
          #print number of vaccinations on a given day
          print("{},{},{}".format(d[0],d[1],d[2]-prev_day_total))
          prev_day_total = d[2]
          prev_type = "vaccination"
        else :
          #print the vaccinations as 0 and increment the infection count for the date
          print("{},{},{}".format(date_of,"vaccination",0))
          count += 1
          prev_type = "infection"
          date_of = d[0]
      elif prev_type == "vaccination":
        # increment the infection type for the given date.
        count += 1
        date_of = d[0]
        prev_type = "infection"
    sys.stdout = temp
    #reset the output and write a completed file.
    print("finished preprocessing data for visualization")

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