最大数 = int(input("いくつまで数えますか？: "))

for 数字 in range(1, 最大数 + 1):
    if 数字 % 15 == 0:
        print("Fizz Buzz")
    elif 数字 % 3 == 0:
        print("Fizz")
    elif 数字 % 5 == 0:
        print("Buzz")
    else:
        print(数字)
