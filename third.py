# Write a program that reads a text file line by line and stores each line in a separate list, within a list.
# Eg.
# Text file content:
# This is line one.
# This is line two.
# This is line three.
# Output:
# [["This is line one"], ["This is line two"], ["This is line three"]]



file=open("data.txt")
lst=list()
for line in file:
    sentence=line.splitlines()
    lst.append(sentence)    
print(lst)