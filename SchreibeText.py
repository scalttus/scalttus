mylist = ["h\nallo", "das", "ist" , "ein"], [ '\n', "test", "noch" ,'\r\n', "mal"]
#
# print(mylist)
listitems = ["ab", "cd", "2", "6"]

with open('abc.txt', 'w') as temp_file:
    for item in listitems:
        temp_file.write("%s\n" % item)
file = open('abc.txt', 'r')
print(file.read())