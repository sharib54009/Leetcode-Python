# LeetCode: pallindrome
# Difficulty: Easy
# Focus: Python basics, loops, conditional statements
def pallindrome(num):
    reversed_num = 0
    numinput = num
    while num > 0:
        digit = num%10
        reversed_num = reversed_num*10 + digit
        num = num//10
    if numinput == reversed_num :
        return "Given number is a palindrome"
    else:
        return "Given number is not a palindrome"
num = int(input("enter a number :"))

result = pallindrome(num)
print(result)