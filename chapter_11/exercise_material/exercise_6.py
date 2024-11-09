import random

def shuffle(tlist):
    n = len(tlist)
    for i in range(n):
        j = random.randint(0, n-1)
        element = tlist.pop(j)
        tlist.append(element)


def main():
    tlist = [1, 2, 3, 4, 5]
    shuffle(tlist)
    print(tlist)

main()