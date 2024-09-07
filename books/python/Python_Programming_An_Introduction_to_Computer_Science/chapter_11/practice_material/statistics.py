import math

def get_numbers():
    nums = []
    num = input("Enter a number, or <Enter> to quit: ")

    while num != "":
        num = float(num)
        nums.append(num)
        num = input("Enter a number, or <Enter> to quit: ")
    return nums

def mean(nums):
    total = 0.0
    for (i) in nums:
        total += i
    return total / len(nums)

def std_dev(nums, avg):
    sum_dev = 0.0
    for (n) in nums:
        dev = avg - n
        sum_dev += dev * dev
    return math.sqrt(sum_dev / (len(nums) - 1))

def median(nums):
    nums.sort()
    size = len(nums)
    mid_pos = size // 2
    if size % 2 != 0:
        med = nums[mid_pos]
    else:
        med = (nums[mid_pos] + nums[mid_pos - 1]) / 2
    return med

def main():
    data = get_numbers()
    avg = mean(data)
    standard_deviation = std_dev(data, avg)
    med = median(data)
    print(f"The average is: {avg}\nThe deviation is: {standard_deviation}\nThe median is: {med}")

if __name__ == "__main__":
    main()