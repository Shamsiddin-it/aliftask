def action_do(inp):
    file = inp[0]
    action = inp[1]
    match action:
        case 'add':
            with open(file, 'a') as new:
                res = input("please write in format: name-price-> ")
                new.writelines("""
""")
                new.write(res)
        case 'change':
            with open(file, 'r') as new:
                res = new.read()
            ch = input("what uou want to change-> ")
            nev = input("enter new data-> ")
            updated = res.replace(ch, nev)
            with open(file, 'w') as new:
                new.write(updated)


inp = [i for i in input().split()]
action_do(inp)

