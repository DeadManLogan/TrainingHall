def remove_duplicates(tlist):
    new = []
    for i in tlist:
        if i not in new:
            new.append(i)

    return new

def main():
    tlist = [1, 1, 1, 2, 3]
    new = remove_duplicates(tlist)
    print(new)

main()