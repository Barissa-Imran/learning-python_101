string = "w3resource"
lst = [1, "'apple'", 4]
tple = (1,"apple", 5666)
if len(string) < 2:
    print("Empty string")
else:
    first_two_char = string[:3]
    last_two_char = string[-2:]
    print(f"{first_two_char}{last_two_char}")
    print(type(lst))
    print(type(tple))   
