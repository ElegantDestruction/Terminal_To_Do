#! /bin/python

# Python script to remove an item
# Get line number to delete
lnum = raw_input('Item to remove > ')

# Create file handler
r_file = open('~/Terminal_To_Do-master/Terminal_To_Do/to_do_list.txt','r+')


def grab_file_contents(r_file,lnum):
    # Create some variables
    i = 1
    line_content = ""

    # Grab the contents of the line to be deleted
    for line in r_file:
        if (str(i) == lnum):
            line_content = line
            return line_content
        else:
            i = i + 1

line_content = grab_file_contents(r_file,lnum)

# Return to the beginning of the file
r_file.seek(0)

# Read all file contents into an array
d = r_file.readlines()

# Return to the beginning of the file
r_file.seek(0)

# Rewrite all lines of the file except the line to be removed
for j in d:
    if (j != line_content):
        r_file.write(j)
r_file.truncate()
r_file.close()
