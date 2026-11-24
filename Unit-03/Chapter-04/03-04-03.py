user_str = input()

result = ""
for character in range(0, len(user_str), 2):
    result += user_str[character]

print(result)