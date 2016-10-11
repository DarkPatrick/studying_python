my_str = input("Enter your string here: ")
answ = list(["It is not palindrome", "It is palindrome"])
print(answ[list(my_str) == list(reversed(my_str))])
