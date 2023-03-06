s = input("Input the string: ").lower()
s_reversed = ''.join(reversed(s))

if s == s_reversed:
    print("The string is palindrome")
else:
    print("The string is NOT palindrome")
