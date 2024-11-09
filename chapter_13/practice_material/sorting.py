def selection(nums):
    n = len(nums)

    for bottom in range(n-1):
        mp = bottom
        for i in range(bottom+1, n):
            if nums[i] < nums[mp]:
                mp = i
        nums[bottom], nums[mp] = nums[mp], nums[bottom]

def merge(lst1, lst2, lst3):
    i1, i2, i3 = 0, 0, 0
    n1, n2 = len(lst1), len(lst2)

    while i1 < n1 and i2 < n2:
        if lst1[i1] < lst2[i2]:
            lst3[i3] = lst1[i1]
            i1 += 1
        else:
            lst3[i3] = lst2[i2]
            i2 += 1
        i3 += 1

    while i1 < n1:
        lst3[i3] = lst1[i1]
        i1 += 1
        i3 += 1
    while i2 < n2:
        lst3[i3] = lst2[i2]
        i2 += 1
        i3 += 1

def merge_sort(nums):
    n = len(nums)

    if n > 1:
        m = n//2
        nums1, nums2 = nums[:m], nums[m:]

        merge_sort(nums1)
        merge_sort(nums2)
        merge(nums1, nums2, nums)

def main():
    nums = [ 2, 216, 65, 65, 654, 98, 6, 31, 7]
    # selection(nums)
    merge_sort(nums)
    print(nums)

if __name__ == "__main__":
    main()