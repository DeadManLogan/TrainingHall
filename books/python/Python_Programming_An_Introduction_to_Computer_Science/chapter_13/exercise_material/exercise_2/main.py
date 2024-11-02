class FibCounter:
    def __init__(self):
        self.count = 0
    
    def get_count(self):
        return self.count
    
    def fib(self, n, depth=0):
        self.count += 1
        indent = " " * depth
        
        print(f"{indent}Computing fib({n})")
        
        if n < 3:
            print(f"{indent}Leaving fib({n}) returning 1")
            return 1

        result = self.fib(n - 1, depth + 1) + self.fib(n - 2, depth + 1)
        print(f"{indent}Leaving fib({n}) returning {result}")
        
        return result
    
    def reset(self):
        self.count = 0

def main():
    fib = FibCounter()
    fib_result = fib.fib(3)
    print(f"\nResult: {fib_result}")
    print(f"The fibonacci function was called {fib.get_count()} times.")

if __name__ == "__main__":
    main()