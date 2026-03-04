import random

# 正解の数字を生成
def generate_number():
    return random.randint(1, 100)

# 判定関数
def judge_guess(guess, target_number):
    if guess > target_number:
        return "too_high"
    elif guess < target_number:
        return "too_low"
    else:
        return "correct"

target_number = generate_number()
max_attempts = 5
result = None  # 判定結果を保存

for attempt in range(1, max_attempts + 1):
    guess = int(input(f"{attempt}回目 数値を入力してください："))
    result = judge_guess(guess, target_number)

    if result == "too_high":
        print("もっと小さいです。")
    elif result == "too_low":
        print("もっと大きいです。")
    elif result == "correct":
        print(f"正解です！答えは {target_number} でした。")
        break

if result != "correct":
    print("ゲームオーバー！")
    print(f"正解は {target_number} でした。")