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

def main():
    # nums = [1,4,2,3,6,5]
    # print(search(7, nums))

    # print(reverse("abc"))
    print(anagram("abc"))

if __name__ == "__main__":
    main()