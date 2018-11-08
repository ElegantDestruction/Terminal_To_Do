#! /bin/python

file = open("~/Terminal_To_Do-master/Terminal_To_Do/to_do_list.txt","r")
count = 1
for line in file:
    print(str(count)+". "+line);
    count = count + 1
file.close()
