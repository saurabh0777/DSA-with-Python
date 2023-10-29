## Delete the specific element in the array
arr = [1,3,5,7,9]
arr.remove(5)
print(arr)

# Removing the element using the index
arr1 =[1,3,4,2,4]
arr1.pop(2)
print(arr1)

# Remove the first occurence of the element 3
# input [1, 3, 5, 3, 7, 1, 9, 3]
# Out [1, 5, 3, 7, 1, 9, 3]

arr2 = [1, 3, 5, 3, 7, 1, 9, 3]
count =0
for i in arr2:
    if i == 3 and count ==0:
        arr2.remove(i)
        count =1
print(arr2)



