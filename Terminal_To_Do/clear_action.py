#! /bin/python


# Python script to clear file contents

# Double check that the user truly wants to clear the file
really = raw_input("Are you sure you want to clear your list? (y/n): ")

if (really == 'y'):
    file = open('~/Terminal_To_Do-master/Terminal_To_Do/to_do_list.txt', 'r+')
    file.truncate(0)
    print("List cleared")
    file.close()
else:
    print("Clear canceled")
