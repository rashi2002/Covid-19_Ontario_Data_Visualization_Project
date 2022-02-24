#!/usr/bin/env python
'''
  Author(s): Andrew Linington (1060878), Griffin Davis (1125177), Rashi Mathur (1125349), Adhyayan Bhandari(1135943)
  Earlier contributors(s): Andrew Hamilton-Wright, Simardeep Singh (1129156)
  Project: Lab Assignment 5 Script (Iteration 0)
  Date of Last Update: Mar 27th, 2021.
  Functional Summary
        Plotting program to plot question 4

  Commandline Parameters: 
    argv[0] = script
    argv[1] = data file
    argv[2] = output file

'''

#
#   Packages and modules
#
import sys



# pandas is a (somewhat slow) library to do complicated
# things with CSV files. We will use it here to identify
# data by column
import pandas as pd

# seaborn and matplotlib are for plotting.  The matplotlib
# library is the actual graphics library, and seaborn provides
# a nice interface to produce plots more easily.
from matplotlib import pyplot as plt


def main(argv):

    '''
    Create a plot using ranks
    '''

    #
    #   Check that we have been given the right number of parameters,
    #
    #   Check that we have been given the right number of parameters,
    #   and store the single command line argument in a variable with
    #   a better name
    #
    if len(argv) != 3:
        print("Usage:",
                "create_name_plot.py <data file> <graphics file>")
        sys.exit(-1)

    csv_filename = argv[1]
    graphics_filename = argv[2]



    #
    # Open the data file using "pandas", which will attempt to read
    # in the entire CSV file
    #
    try:
        csv_df = pd.read_csv(csv_filename)

    except IOError as err:
        print("Unable to open source file", csv_filename,
                ": {}".format(err), file=sys.stderr)
        sys.exit(-1)


    # A this point in the file, we begin to do the plotting

    # We must get the figure before we plot to it, or nothing will show up.
    # The matplotlib "figure" is the data environment that we are drawing
    # our plot into.  The seaborn library will draw onto this figure.
    # We don't see seaborn directly refer to "fig" because it is internally
    # drawing on "the current figure" which is the same one we are
    # referencing on this line.
    fig = plt.figure()

    # This creates a lineplot using seaborn.  We simply refer to
    # the various columns of data we want in our pandas data structure.
    # sns.histplot(x="Age group", data = csv_df, bins =9, log_scale=None, stat="count")

    # sns.barplot(x = "Age group", y = "Count", data = csv_df)


        

        


    data = csv_df.groupby("Age group")["Count"].sum()#Getting the data for the pie graph
    textprops = {"fontsize":5} # Font size of text in pie chart
    explode=(0, 0.1,0, 0, 0, 0, 0, 0, 0)#Seperate the second section from the rest(visual effect)
    plt.title("Case Count by Age Group")#Creates a title for the graph
    data.plot.pie(autopct="%.1f%%", explode=explode, textprops = textprops);#Creating the pie graph

 


    # Now we can save the matplotlib figure to a file

    fig.savefig(graphics_filename, bbox_inches="tight")


    # Uncomment this line to show the figure on the screen.  Note
    # that in repl.it, you may not be able to close the figure (it may
    # be too big for your screen) so you will have to press [CTRL]-C
    # in order to stop your program in order to be able to run commands
    # in your shell again.
    # plt.show()

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
