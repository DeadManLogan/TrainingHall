def inner_prod(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must have same length.")
    
    return (sum(a * b for a, b in zip(list1, list2)))

def main():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    print(inner_prod(list1, list2))

main()