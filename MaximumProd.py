#. Write a Python program to find a pair with the highest product from a given array of integers.
#Original array: [1, 2, 3, 4, 7, 0, 8, 4]
#Maximum product pair is: (7, 8)
#Original array: [0, -1, -2, -4, 5, 0, -6]
#Maximum product pair is: (-4, -6)

def find_highest_product_pair_op(nums):
    nums.sort()
    return max(nums[0]*nums[1],nums[-1]*nums[-2])
def find_highest_product_pair(nums):
    if len(nums) < 2:
        return "Array should have at least two elements"

    nums.sort()

    first_ele = nums[0] * nums[1]
    last_ele = nums[-1] * nums[-2]
    if first_ele> last_ele:
        return (nums[0],nums[1])
    else:
        return  (nums[-1] + nums[-2])


# Example usage

nums = [0, -1, -2, -4, 5, 0, -6]

result = find_highest_product_pair(nums)
print("Pair with the highest product:", result)