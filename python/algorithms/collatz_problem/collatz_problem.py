def collatz(number: int):
    while number > 1:
        if (number % 2 == 0):
            number = number // 2
        else:
            number = 3 * number + 1
    return number

if __name__ == "__main__":
    result = None
    while result is None:
        try:
            input_num = input("Input: ")
            result = collatz(int(input_num))
            print(f"input is {input_num}, result is {result}")
        except ValueError:
            print("Input must be a valid integer")
