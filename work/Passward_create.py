import string
import random

def create_password(length, use_upper, use_digit):

    if use_upper == "y" and use_digit == "y":
        randlst = [random.choice(string.ascii_letters + string.digits) for i in range(length)]
    elif use_upper == "y" :
        randlst = [random.choice(string.ascii_letters) for i in range(length)]
    elif use_digit == "y":
        randlst = [random.choice(string.ascii_lowercase + string.digits) for i in range(length)]
    else :
        randlst = [random.choice(string.ascii_lowercase) for i in range(length)]
    

    return ''.join(randlst)

length = int(input("文字数："))

use_upper = input("大文字あり（Y/N）：").lower()
while use_upper != "y" and use_upper != "n":
    print("y か n を入力してください")
    use_upper = input("大文字あり（Y/N）：").lower()

use_digit = input("数字あり（Y/N）：").lower()
while use_digit != "y" and use_digit != "n":
    print("y か n を入力してください")
    use_digit = input("数字あり（Y/N）：").lower()

password = create_password(length, use_upper, use_digit)

print(password)