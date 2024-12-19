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
        case 'del':
            with open(file, 'r') as fle:
                res = fle.read()
            choosed = input("enter data you want to delete-> ")
            updated = res.replace(choosed, '')
            with open(file, 'w') as new:
                new.write(updated)
        case "sum":
            with open(file, 'r') as new:
                res = new.readlines()
                mylist = []
            for i in res:
                mylist.append(i.split('-'))
            sum = 0
            for j in mylist:
                   sum+=int(j[1])
            print(sum)

while True:
    inp = [i for i in input("Enter name of file and action, if you want to quit programm write break: ").split()]
    if inp==['break']:
        break
    action_do(inp)

