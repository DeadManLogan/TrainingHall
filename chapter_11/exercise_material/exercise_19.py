class Set():
    def __init__(self, elements):
        if elements is None:
            self.elements = []
        else:
            self.elements = list(set(elements))

    def add_element(self, x):
        self.elements.append(x)

    def delete_element(self, x):
        if x in self.elements:
            self.elements.remove(x)

    def member(self, x):
        if x in self.elements:
            return True
        else:
            return False
        
    def intersection(self, set2):
        self.intersect_set = []
        for (i) in self.elements:
            if i in set2.elements:
                self.intersect_set.append(i)
        return Set(self.intersect_set)
    
    def union(self, set2):
        all_elements = list(set(self.elements + set2))
        return Set(all_elements)
    
    def subtract(self, set2):
        unique_elements = [el for el in self.elements if el not in set2]
        return Set(unique_elements)
    
    def __str__(self):
        return "{" + ", ".join(str(e) for e in self.elements) + "}"
    
if __name__ == "__main__":
    set1 = Set([1, 2, 3, 4])
    set2 = Set([3, 4, 5, 6])


    print("Set 1:", set1)
    print("Set 2:", set2)

    set1.add_element(5)
    print("Set 1 after adding 5:", set1)

    set1.delete_element(2)
    print("Set 1 after deleting 2:", set1)

    print("Is 3 a member of Set 1?", set1.member(3))
    print("Is 7 a member of Set 1?", set1.member(7))

    intersection_set = set1.intersection(set2)
    print("Intersection of Set 1 and Set 2:", intersection_set)

    union_set = set1.union(set2)
    print("Union of Set 1 and Set 2:", union_set)

    subtract_set = set1.subtract(set2)
    print("Set 1 subtracting Set 2:", subtract_set)
