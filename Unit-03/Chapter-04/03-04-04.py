user_str = input()
result = ""
for character in range(len(user_str)):
    if user_str[character] == " ":
        if result == "":
            result = str(character)
        else:
            result = result + ", " + str(character)

if result == "":
    print("no spaces found")
else:
    print(result)
