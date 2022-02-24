#!/usr/bin/env python

'''
linePlotVisualization.py
  Author(s): Andrew Linington (1060878), Griffin Davis (1125177), Rashi Mathur (1125349)
  Earlier contributors(s): Andrew Hamilton-Wright, Simardeep Singh (1129156)
  Project: Question 3
  Date of Last Update: Mar 27th, 2021.

  Functional Summary
      Plotting program to plot the data for Question 3

     Commandline Parameters: 1
        argv[1] = data file
        argv[2] = output file
        argv[3] = type of Question
'''


#   Packages and modules

import sys

# pandas is a (somewhat slow) library to do complicated
# things with CSV files. We will use it here to identify
# data by column
import pandas as pd

# seaborn and matplotlib are for plotting.  The matplotlib
# library is the actual graphics library, and seaborn provides
# a nice interface to produce plots more easily.
import seaborn as sns
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker


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
    if len(argv) != 4:
        print("Usage:",
                "linePlotVisualization.py <data file> <graphics file> <Question (Q3/Q2)>")
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


    if argv[3] == "Q3":
      ax = sns.lineplot(x = "Date", y = "Count", hue="Type", data=csv_df)
      plt.xticks(rotation = 45, ha = 'right')
      ax.xaxis.set_major_locator(ticker.MaxNLocator(8))
    elif argv[3] == "Q2":
      ax = sns.lineplot(x = "Date", y = "Count", hue="PHU_Id", data=csv_df)
      plt.xticks(rotation = 45, ha = 'right')
      ax.xaxis.set_major_locator(ticker.MaxNLocator(8))
    else:
      print("Usage:", "Please specify the proper question.")
      sys.exit(1)


    # Now we can save the matplotlib figure that seaborn has drawn
    # for us to a file
    fig.savefig(graphics_filename, bbox_inches="tight")


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
