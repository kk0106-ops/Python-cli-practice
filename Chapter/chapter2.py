year = 2024

if year % 400 == 0:
    print(f"{year}は閏年です。")
elif year % 100 == 0:
    print(f"{year}は平年です。")
elif year % 4 == 0:
    print(f"{year}は閏年です。")
else :
    print(f"{year}は平年です。")