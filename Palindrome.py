
def check_palindrome(s):

    if s==s[::-1]:
        return True
    else:
        False

str=input("Enter a string:")
if(check_palindrome(str)):
    print("string is palindrome")
else:
    print("string is not palindrome")
