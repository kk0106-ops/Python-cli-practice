import json
import os
import datetime

FILE_NAME = 'records.json'

# 保存
def save_records(records):
    with open(FILE_NAME, 'w') as f:
        json.dump(records, f, indent=2)

# ファイル読み込み
def load_records():
    if os.path.isfile(FILE_NAME):
        try:
            with open(FILE_NAME, 'r') as f:
                return json.load(f)
        except json.decoder.JSONDecodeError:
            print("records.jsonに問題が発生したため、初期化します。")
            return []
    else:
        return []

# メニュー
def show_menu():
    print("\n-----家計簿メニュー-----")
    print("1. 収入の追加")
    print("2. 支出の追加")
    print("3. 記録の一覧表示")
    print("4. 記録の削除")
    print("5. 合計金額の表示")
    print("6. 終了")

# 金額入力
def input_amount():
    while True:
        amount_input = input("金額を入力してください：")
        if not amount_input.isdigit():
            print("\n数字を入力してください。")
            continue
        return int(amount_input)

# 番号入力
def input_index():
    while True:
        index = input("番号を入力してください：")
        if not index.isdigit():
            print("\n数値を入力してください。")
            continue
        return int(index)

# 収支追加
def add_income_expense(choice, records):
    amount = input_amount()
    memo = input("メモを入力してください：")
    today = str(datetime.date.today())

    record_type = "income" if choice == "1" else "expense"

    record = {
        "type": record_type,
        "amount": amount,
        "memo": memo,
        "date": today
    }

    records.append(record)
    save_records(records)
    print("\n収支を追加しました。")

# 表示
def show_records(records):
    type_map = {
        "income": "収入",
        "expense": "支出"
    }

    if not records:
        print("\n記録がありません。")
        return

    print("\n-----記録の一覧表示------")
    for i, item in enumerate(records, 1):
        type_jp = type_map.get(item["type"], "不明")
        print(f"{i:>2}. {type_jp:<2} | 金額：{item['amount']:>6}円 | メモ：{item['memo']:<10} | 日付：{item['date']}")
    print("------------------------")

# 削除
def delete_record(records):
    show_records(records)
    if not records:
        return

    index = input_index()
    i = index - 1

    if 0 <= i < len(records):
        records.pop(i)
        save_records(records)
        print(f"\n記録{index}番を削除しました。")
    else:
        print("\n無効な番号です。")

# 合計
def show_total(records):
    income_total = 0
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

# メイン
def main():
    records = load_records()

    while True:
        show_menu()
        choice = input("番号を入力してください：")

        if choice in ["1", "2"]:
            add_income_expense(choice, records)
            show_records(records)

        elif choice == "3":
            show_records(records)

        elif choice == "4":
            delete_record(records)

        elif choice == "5":
            show_total(records)

        elif choice == "6":
            print("\n終了します。")
            break

        else:
            print("\n無効な選択です。")

# 実行
if __name__ == "__main__":
    main()