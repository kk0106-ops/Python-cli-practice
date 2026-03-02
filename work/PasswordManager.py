passwords = []

while True:
    print("1：追加")
    print("2：一覧")
    print("3：終了")

    choice = input("選択してください：")

    if choice == "1":
        service = input("サービス名：")
        user_id = input("ID：")
        password = input("パスワード：")
        passwords.append([service, user_id, password])

    elif choice == "2":
        if not passwords:
            print("データがありません")
        else:
            for i in range(len(passwords)):
                for f in range(len(passwords)):
                    print(f"{f + 1}件目")
                    print(f"サービス：{passwords[i][f]}")
                    print(f"ID：{passwords[i][f]}")
                    print(f"パスワード：{passwords[i][f]}")

    elif choice == "3":
        break