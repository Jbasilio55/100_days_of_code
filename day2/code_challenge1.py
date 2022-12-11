# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

# Warning. Do not change the code on lines 1-3. Your program should work for different inputs. e.g. any two-digit number.

str_num = input("Type a two digit number: ")
total = int(str_num[0]) + int(str_num[1])
print(total)