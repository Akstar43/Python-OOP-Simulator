y = 5
x = 5

i = 0
limit = 10
while i < limit:
    brick = "[!]" * x
    print(f'{brick}\n' * y)
    y -= 1
    x -= 1
    if y == 0:
        print("Broken")
        y = 5
        x = 5
    if i == limit:
        x = 0
        y = 0
        continue
    i += 1




