#### Reverse Linked List ####

# Write a program to reverse a linked list #

# MyAnswer:
'''
import pandas as pd
import numpy as np

llist = [25,6,8,40]
print(llist)
data_frame = pd.DataFrame(llist)
data_frame = data_frame.iloc[::-1]
print("Print Reversed List")
print(data_frame.iloc[:,0].tolist())
'''

# Answer 1: Iterative Method,
	# Iterate trough the linked list. 
	# In loop, change next to prev, prev to current and current to next.

# Python program to reverse a linked list 
# Time Complexity : O(n)
# Space Complexity : O(1)
 
# Node class 
class Node:
 
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
 
    # Function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
         
    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print temp.data,
            temp = temp.next
 
 
# Driver program to test above functions
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)
 
print "Given Linked List"
llist.printList()
llist.reverse()
print "\nReversed Linked List"
llist.printList()
 
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)





