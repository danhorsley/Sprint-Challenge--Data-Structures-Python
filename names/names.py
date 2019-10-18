import time
from binary_search_tree import *

start_time = time.time()
bst1 = BinarySearchTree('mmm')
bst2 = BinarySearchTree('lll')

f = open('names_1.txt', 'r')
#names_1 = f.read().split("\n")  # List containing 10000 names
for item in f.read().split("\n"):
    bst1.insert(item)
f.close()

f = open('names_2.txt', 'r')
#names_2 = f.read().split("\n") 
for item in f.read().split("\n"):
    bst2.insert(item) # List containing 10000 names
f.close()

duplicates = []

#Commentary on run time
## The run time complexity of this original code (bubble search) goes up by multiplying the length of each list, n*n, in this case 
## it is 10,000 * 10,000 or O(n^2) in the notation.  with a binary search tree one can achieve run time 
## run time complexity of O(log n)


# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
def in_bst2(some_item):
    if bst2.contains(some_item):
        return duplicates.append(some_item)
    else:
        return None

bst1.for_each(in_bst2)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

