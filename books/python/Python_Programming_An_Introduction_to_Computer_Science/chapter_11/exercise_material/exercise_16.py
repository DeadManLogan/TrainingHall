import statistics

class StatSet:
    def __init__(self):
        self.stat_set = []
    
    def add_number(self, x):
        self.stat_set.append(x)
    
    def mean(self):
        self.stat_mean = sum(self.stat_set)/len(self.stat_set)
        return self.stat_mean
    
    def median(self):
        self.stat_median = statistics.median(self.stat_set)
        return self.stat_median
    
    def std_dev(self):
        self.stat_std = statistics.stdev(self.stat_set)
        return self.stat_std
    
    def count(self):
        return len(self.stat_set)
    
    def min(self):
        return min(self.stat_set)
    
    def max(self):
        return max(self.stat_set)
    
if __name__ == "__main__":
    stats = StatSet()
    
    numbers = [10, 20, 30, 40, 50]
    
    for number in numbers:
        stats.add_number(number)
    
    # Displaying statistics
    print("Count:", stats.count())
    print("Mean:", stats.mean())
    print("Median:", stats.median())
    print("Standard Deviation:", stats.std_dev())
    print("Minimum:", stats.min())
    print("Maximum:", stats.max())
