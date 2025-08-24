def reverse_string(s: str) -> str:
    return s[::-1]
print(reverse_string(input("Write a Word")))
def mean(nums: list) -> float:
    if not nums:
        raise ValueError("The list is empty, cannot compute mean.")

    return sum(nums) / len(nums)
