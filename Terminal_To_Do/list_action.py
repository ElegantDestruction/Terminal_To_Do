#! /bin/python

file = open("to_do_list.txt","r")
count = 1
for line in file:
    print(str(count)+". "+line);
    count = count + 1
file.close()
