def search(x, nums):
    try:
        return nums.index(x)
    except:
        return -1

def reverse(s):
    if s == "":
        return s
    else:
        return reverse(s[1:]) + s[0]
    
def anagram(s):
    if s == "":
        return [s]
    else:
        ans = []
        for word in anagram(s[1:]):
            for position in range(len(word) + 1):
                ans.append(word[:position] + s[0] + word[position:])
        return ans
    
def rec_binary(x, nums, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    item = nums[mid]
    if item == x:
        return mid
    elif x < item:
        return rec_binary(x, nums, low, mid-1)
    else:
        return rec_binary(x, nums, mid+1, high)

def loop_power(a, n):
    ans = 1
    for i in range(n):
        ans *= a
    return ans

def rec_power(a, n):
    if n == 0:
        return -1
    else:
        factor = rec_power(a, n//2)
        if n%2 == 0:
            return factor * factor
        else:
            return factor * factor * a

def search(x, nums):
    return rec_binary(x, nums, 0, len(nums) - 1)

def fib(n):
    if n < 3:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def main():
    nums = [1,4,2,3,6,5]
    # print(search(7, nums))

    # print(reverse("abc"))
    # print(anagram("abc"))
    # print(loop_power(2, 3))
    # print(search(6, nums))
    print(fib(15))

if __name__ == "__main__":
    main()