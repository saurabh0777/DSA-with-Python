# Write a Python program to insert a newly created item before the second element in an existing array.
#Original array: array('i', [1, 3, 5, 7, 9])
# Insert new value 4 before 3:
#New array: array('i', [1, 4, 3, 5, 7, 9])

arr = [1,3,5,7,9]
ind = arr.index(3)
arr.insert(ind,4)
print(arr)

