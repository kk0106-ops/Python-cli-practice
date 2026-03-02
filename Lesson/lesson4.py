def is_leep_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

year = 2024
result = is_leep_year(year)
print(result)