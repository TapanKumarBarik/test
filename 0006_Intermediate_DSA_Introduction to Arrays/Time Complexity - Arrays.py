"""
What is the time complexity for inserting/deleting at the beginning of the array?
"""
#Demonstarte it in below
#O(n) - because we have to shift all the elements
#O(1) - because we can insert at the end of the array without shifting any elements

#python example
def insert_at_beginning(arr, element):
    arr.insert(0, element)  # O(n) time complexity
    return arr
def delete_at_beginning(arr):
    if len(arr) > 0:
        arr.pop(0)  # O(n) time complexity
    return arr