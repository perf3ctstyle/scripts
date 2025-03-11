# Input: string
# Output: boolean
# Description: returns the result of verifying whether the input string is a palindrome
def verify_palindrome(input: str):
    if input is None:
        return False
    leftIndex = 0
    rightIndex = len(input) - 1
    while leftIndex < rightIndex:
        if input[leftIndex] != input[rightIndex]:
            return False
        leftIndex += 1
        rightIndex -= 1
    return True

if __name__ == "__main__":
    verify_palindrome("123")
    verify_palindrome("111")
    verify_palindrome("aaa b")
    verify_palindrome("")
    verify_palindrome(" ")
    verify_palindrome("madam")
    verify_palindrome("nurses run")
    