# write your code here
taken = "         "
li1 = [[taken[x] for x in range(j, j + 3)] for j in range(0, len(taken), 3)]
space = 0


def show(li1):
    print("---------")
    for i in range(len(li1)):
        print(f'| {li1[i][0]} {li1[i][1]} {li1[i][2]} |')
    print("---------")


def check(li1):
    for j in li1:
        if j[0] == j[1] == j[2] != " ":
            winningr = j[0]
            return ("{} wins".format(winningr))

    for i in range(3):
        if li1[0][i] == li1[1][i] == li1[2][i] != " ":
            winningc = li1[0][i]
            return "{} wins".format(winningc)


    if li1[0][0] == li1[1][1] == li1[2][2] != " ":
        return "{} wins".format(li1[0][0])

    if li1[2][0] == li1[1][1] == li1[0][2] != " ":
        return "{} wins".format(li1[1][1])

    spc = [x for y in li1 for x in y if x == " "]
    if len(spc) > 0:
        return "Game not finished"

    return "Draw"

show(li1)
count = 0
while True:
    spc = [x for y in li1 for x in y if x == " "]
    if len(spc) > 0:
        try:
            coordx, coordy = input("Enter the coordinates:").split()
            coordx, coordy = int(coordx), int(coordy)
        except:
            print("You should enter numbers!")
            continue
        if coordx not in (1, 2, 3) or coordy not in (1, 2, 3):
            print("Coordinates should be from 1 to 3!")
            continue
        if li1[3 - coordy][coordx - 1] != " ":
            print("This cell is occupied! Choose another one!")
            continue
        else:
            while count < 9:
                if count % 2 == 0:
                    li1[3 - coordy][coordx - 1] = "X"
                    break
                else:
                    li1[3 - coordy][coordx - 1] = "O"
                    break
            c = check(li1)
            count += 1
            show(li1)
            if c != "Game not finished":
                print(c)
                break
            else:
                continue

    else:
        break

