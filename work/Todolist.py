import json
import os

def save_task(task_save):
    with open('task.json', 'w') as f:
        json.dump(task_save, f, indent = 2)

def add_task(a_task):
    print("")
    while True:
        task_in = input("追加するタスクを入力してください：")
        if task_in == "":
            print("空文字の入力はできません")
        else:
            break

    a_task.append(task_in)
    save_task(a_task)
    print(f"タスクを追加しました：{task_in}")

def show_task(s_task):
    print("----タスク一覧----")
    for i in range(len(s_task)):
        print(f"{i + 1}:{s_task[i]}")

def delete_task(d_task):
    cancel_num = len(d_task) + 1
    print("----タスク一覧----")
    for i in range(len(d_task)):
        print(f"{i + 1}:{d_task[i]}")
    print(f"{cancel_num}:キャンセル")

    while True:
        try:
            task_number = int(input("削除するタスクの番号を入力してください："))

            if task_number == cancel_num:
                break

            if 1 <= task_number and task_number <= len(d_task):
                old_task = d_task.pop(task_number - 1)
                save_task(d_task)
                print(f"タスクを削除しました：{old_task}")
                break
            else:
                print("タスク番号範囲外です。再度入力してください")
                continue
        except ValueError:
            print("タスク番号を入力してください")

task = []

if os.path.isfile('task.json'):
    try:
        with open('task.json', 'r') as f:
            task = json.load(f)
    except json.decoder.JSONDecodeError:
        print("task.jsonに問題が発生したため、新しく作成しなおします。")

save_task(task)

while True:
    print("----メニュー----")
    print("1.タスクの追加")
    print("2.タスクの表示")
    print("3.タスクの削除")
    print("4.終了")

    
    select = input("選択肢を入力してください：")
    if select not in ("1", "2", "3", "4"):
        print("1~4のみ入力してください")
        continue

    if select == "1":
        add_task(task)

    elif select == "2":
        if not task:
            print("タスクがありません")
            print("タスクを追加してください")
        else:
            show_task(task)

    elif select == "3":
        if not task:
            print("削除するタスクがありません")
        else:
            delete_task(task)

    elif select == "4":
        break