import json
import os
import datetime

# records.jsonに保存
def save_records(records):
    with open('records.json', 'w') as f:
        json.dump(records, f, indent = 2)

# メニューの表示
def show_menu():
    print("\n-----家計簿メニュー-----")
    print("1. 収入の追加")
    print("2. 支出の追加")
    print("3. 記録の一覧表示")
    print("4. 記録の削除")
    print("5. 合計金額の表示")
    print("6. 終了")

# 収支の追加
def add_income_expense(choice, records, amount, memo):
    today = str(datetime.date.today())
    if choice == "1":
        dictionary = {
            "type"   : "income",
            "amount" : amount,
            "memo"   : memo,
            "date"   : today
        }
    elif choice == "2":
        dictionary = {
        "type"   : "expense",
        "amount" : amount,
        "memo"   : memo,
        "date"   : today
    }

    records.append(dictionary)
    save_records(records)
    print("\n収支を追加しました。")

# 記録一覧の表示
def show_records(records):
    type_map = {
        "income"  : "収入",
        "expense" : "支出"
    }

    if not records:
        print("\n記録がありません。")
        return

    print("\n-----記録の一覧表示------")
    for i, item in enumerate(records, 1):
        type_jp = type_map.get(item["type"], "不明")
        print(f"{i:>2}. {type_jp:<2} | 金額：{item['amount']:>6}円 | メモ：{item['memo']:<10} | 日付：{item['date']}")
    print("------------------------")

# 記録の削除
def delete_record(records, index):
    i = index -1
    if 0 <= i < len(records):
        records.pop(i)
        save_records(records)
        print(f"\n記録{index}番を削除しました。")

    else:
        print("\n無効な番号です。")

# 合計金額の表示
def show_total(records):
    income_total  = 0
    expense_total = 0

    for item in records:
        if item["type"] == "income":
            income_total += item["amount"]
        elif item["type"] == "expense":
            expense_total += item["amount"]

    print("\n-----合計収入-----")
    print(f"金額：{income_total}円")
    print("\n-----合計支出-----")
    print(f"金額：{expense_total}円")
    print("\n-----差額-----")
    print(f"金額：{income_total - expense_total}円")

records = []

# メイン処理
if os.path.isfile('records.json'):
    try:
        with open('records.json', 'r') as f:
            records = json.load(f)
    except json.decoder.JSONDecodeError:
        print("records.jsonに問題が発生したため、新しく作成しなおします。")

save_records(records)

while True:
    show_menu()
    choice = input("番号を入力してください：")

    if choice in ["1", "2"]:
        amount = int(input("金額を入力してください："))
        memo   = input("メモを入力してください：")
        add_income_expense(choice, records, amount, memo)
        show_records(records)

    elif choice == "3":
        show_records(records)

    elif choice == "4":
        show_records(records)
        index = input("削除する記録の番号を入力してください：")
        if index.isdigit():
            delete_record(records, int(index))
            show_records(records)
        else:
            print("\n数値を入力してください。")

    elif choice == "5":
        show_total(records)
    elif choice == "6":
        print("\n終了します。")
        break
    else:
        print("\n無効な選択です。")
        continue