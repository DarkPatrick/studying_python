my_str = input("Enter your string here: ")
print(''.join(list(filter(lambda user_char: (user_char not in '''!()-[]{};:'"\,<>./?@#$%^&*_~'''), my_str))))
