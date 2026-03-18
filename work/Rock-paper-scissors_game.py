import random

def opponent_hand():
    return random.randint(1, 3)

def judge_function(e_hand, i_hand):
    if i_hand == e_hand:
        return "draw"
    elif i_hand == 1 and e_hand == 2 or i_hand == 2 and e_hand == 3 or i_hand == 3 and e_hand == 1:
        return "victory"
    else:
        return "lose"

# 手の辞書
hands = {
    1: "グー",
    2: "チョキ",
    3: "パー"
}

print("--じゃんけん表--")
print("1:グー")
print("2:チョキ")
print("3:パー")

print("じゃんけん")

while True:
    e_hand = opponent_hand()
    i_hand = int(input())

    if i_hand not in (1, 2, 3):
        print("1～3のみ入力して下さい")
        continue

    print(f"あなた：{hands[i_hand]}")
    print(f"相手：{hands[e_hand]}")

    defeat = judge_function(e_hand, i_hand)

    if defeat == "draw":
        print("あいこで")
    elif defeat == "victory":
        print("勝利！")
        break
    else:
        print("負け")
        break