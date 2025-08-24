def reverse_string(s: str) -> str:
    return s[::-1]
print(reverse_string(input("Write a Word\n")))

from array import array

def mean(nums: array) -> float:
    if not nums:
        raise ValueError("The array is empty, cannot compute mean.")
    return sum(nums) / len(nums)
user_input = input("Enter numbers separated by spaces: ")
nums = array('i', [int(x) for x in user_input.split()])
print("The mean is:", mean(nums))
