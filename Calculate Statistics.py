def calculate_stats(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    minimum = min(numbers)
    maximum = max(numbers)

    print(f"Numbers: {numbers}")
    print(f"Sum:     {total}")
    print(f"Count:   {count}")
    print(f"Average: {average:.2f}")
    print(f"Min:     {minimum}")
    print(f"Max:     {maximum}")


numbers = [10, 25, 3, 47, 8, 16, 32]
calculate_stats(numbers)
