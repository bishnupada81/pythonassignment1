# Finally, I'll share a CSV file here with you, write a program to read the CSV file line by line, split each line into separate values based on the character , (comma) and store them in a list of list like in problem 4.
# Eg.
# Text file content:
# 1,2,3,4
# 5,6,7,8
# 9,10,11,12
# Output:
# [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]] (edited) 

import csv

with open('leukemia_small.csv','rt')as f:
  data = csv.reader(f)
  my_list=[]
  for row in data: 
    my_list.append(row)
  print(my_list)
