# Write a program that reads a text file line by line, splits each line into separate words, stores words in lists, within lists.
# Eg.
# Text file content:
# This is line one.
# This is line two.
# This is line three.
# Output:
# [["This", "is", "line", "one"], ["This", "is", "line", "two"], ["This", "is", "line", "three"]]

file=open("data.txt")
lst=list()
for line in file:
    word=line.split()
    lst.append(word)    
print(lst)