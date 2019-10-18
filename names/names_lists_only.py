import time
from binary_search_tree import *

start_time = time.time()
bst1 = BinarySearchTree('mmm')
bst2 = BinarySearchTree('lll')

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names

f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n") 

f.close()


#duplicates = []
#if i am reading the rubric right i can use and standard python collection here so i can use set. 
#this is way way faster reaching run times of 1 hundreth of a second even on my slow laptop which
#was doing 12 seconds for the original bubble search
# i did consider doing an in place merge sort but that was too slow
duplicates = list(set(names_1).intersection(set(names_2)))



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")