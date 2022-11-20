
Problems:
Task 2:
Deleting the linked list results in a linked list of 1, containing a number i believe to be assosiated with the memory allocation.


Task 3

Task                   Array list:     Linked list:    Items used: (array, linked):
Appending from back    117.006 ms      516.03 ms       10m, 10m
indexing:              41.003 ms       153.008 ms      10m, indexing 10k
insert, front;         2587.15 ms      60.004 ms       100, 1m
insert, middle:        1264.07 ms      1680.1 ms       100, 100
remove, front:         2338.13 ms      36.002 ms       100, 1m
remove, middle:        1200.07 ms      1644.09 ms      100, 100
remove, end;           7.001 ms        37.002 ms       1m, 1m

-Appending from back:
Array were more efficient, as the process of construction is less complex, no creating nodes or keeping track of that.

-Indexing;
Indexing from array is a matter of calling the data entry, while from linked list it's a loop through the nodes. Linked list weree
extremely less efficient.

-Inserting at front:
Inserting at front in an array results in the entire array being shifted and rewritten, while linked list just inserts at front and updates 
surrounding nodes, being much more efficient.

-Inserting at middle:
Both array and linked list has great difficoulty inserting at the middle, as both classes uses for loops for either rewriting later data (array) 
or finding n'th entry (linked list)

-Remove from front:
Linked list much more efficient, same reason as for inserting.

-Remove from middle: 
Both performed porly, same reason as insertign from middle.

-Remove from end:
Both classes were effectove, array somewhat more, same reason as for appending from back

-Print:
I were not able to properly find a way to time the performance of the print function :(








Task 4g:
For n = 68, k = 7, a smart man like Josephus would stand at the end of the circle, at position nr. 68 to survive.