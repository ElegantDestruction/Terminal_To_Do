#! /bin/python
# Python script to append an item to the list

new_item = raw_input('New Item > ')

file = open('~/Terminal_To_Do-master/Terminal_To_Do/to_do_list.txt', 'a+')
file.write(new_item+'\n')
file.close()
