def main():
    # Prompt the user to enter a string
    s = input().strip()
    print(isPalindrome(s))

# Check if a string is a palindrome 
def isPalindrome(s):
   l = len(s)
   for i in range(l // 2):
       if s[i] != s[l - i - 1]:
           return False
   return True


main() # Call the main

