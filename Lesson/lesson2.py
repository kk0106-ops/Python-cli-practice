def print_hello():
    print("こんにちは!")

print_hello()

def add_sub_numbers(a, b):
    c = a + b
    d = a - b
    return c, d

added, subed = add_sub_numbers(b = 10,a = 100)
print(added, subed)
