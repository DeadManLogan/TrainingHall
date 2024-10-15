def search(x, nums):
    try:
        return nums.index(x)
    except:
        return -1

def main():
    nums = [1,4,2,3,6,5]
    print(search(7, nums))

if __name__ == "__main__":
    main()