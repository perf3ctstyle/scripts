# Find the sum of all natural numbers that are multiples of 3 and 5 under 1000

def find_sum_of_multiples_for(number: int, threshold: int):
    sum = 0
    multiplier = 1
    while number * multiplier < threshold:
        sum += number * multiplier
        multiplier += 1
    return sum

def find_sum_of_all_multiples_under(threshold: int):
    sum = find_sum_of_multiples_for(3, threshold)
    sum += find_sum_of_multiples_for(5, threshold)
    sum -= find_sum_of_multiples_for(15, threshold)
    return sum

if __name__ == "__main__":
    threshold = 1000
    sum = find_sum_of_all_multiples_under(threshold)
    print(f"Sum of all multiples under {threshold} is {sum}")

# Result: found a medium optimal solution, but with a bug: there are intersections in some multiples of 3 and 5 (for example, 15), which led to incorrect answer
