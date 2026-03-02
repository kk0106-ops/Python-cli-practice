def Num_Input():
    i = 1

    while True:
        num = input( i + "回目：数値を入力してください")
        if num.isdigit():
            total_num = int(num)
        else:
            print("再度、数値を入力してください：")

        operator: str = input("演算子を入力してください (+, -, *, /)：")

        if operator in ["+", "-", "*", "/"]:
            return num
        else:
            print("演算子以外が入力されました。")

def calculation(num_value, num_value2, operator):
#フラグ 0:成功 1:0による計算エラー
    if operator == "+":
        return 0, num_value + num_value2

    elif operator == "-":
        return 0, num_value - num_value2

    elif operator == "*":
        return 0, num_value * num_value2

    elif operator == "/":
        if num_value2 == 0:
            return 1, None

        else:
            return 0, num_value / num_value2

num1, num2, operator = Num_Input()

flag, answer = calculation(num1, num2, operator)

if flag == 0:
    print("結果",answer)

elif flag == 1:
    print("0では割り切れません")