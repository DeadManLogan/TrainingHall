def count(tlist, x):
    res = 0
    for i in range(len(tlist)):
        if x == tlist[i]:
            res += 1
    return res

def is_in(tlist, x):
    if x in tlist:
        return True
    else:
        return False
    
def index(tlist, x):
    for i in range(len(tlist)):
        if x == tlist[i]:
            return i
        
def reverse(tlist):
    temp_list = []
    for i in range(len(tlist) - 1, -1, -1):
        temp_list.append(tlist[i])
    return temp_list

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        sort(array, low, pi - 1)
        sort(array, pi + 1, high)


def main():
    tlist = ['z', 'b', 'a']
    sort(tlist, 0, len(tlist)-1)
    print(tlist)

main()