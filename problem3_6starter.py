# -problem3_6.py *- coding: utf-8 -*-

# Import modules needed in this program
import sys

# Open the files which names are passed in
infile = open(sys.argv[1])
outfile = open(sys.argv[2], 'w')

# Process the input file and write the results to the output file
for line in infile:
    outfile.write(str(len(line.strip("\n"))) + "\n")

# Close the files
infile.close()
outfile.close()