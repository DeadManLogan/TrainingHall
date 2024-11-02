fib_3_count = 0

def fib(n, depth=0):
    global fib_3_count

    indent = " " * depth
    
    print(f"{indent}Computing fib({n})")

    if n == 3:
        fib_3_count += 1
    
    if n < 3:
        print(f"{indent}Leaving fib({n}) returning 1")
        return 1

    result = fib(n - 1, depth + 1) + fib(n - 2, depth + 1)
    print(f"{indent}Leaving fib({n}) returning {result}")
    
    return result

def main():
    fib_result = fib(3)
    print(f"\nResult: {fib_result}")
    print(f"fib(3) was computed {fib_3_count} times.")

if __name__ == "__main__":
    main()