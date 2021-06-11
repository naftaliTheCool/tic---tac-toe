def print_board():
    print(y[0])
    print(y[1])
    print(y[2])
u = [1,2,3,4,5,6,7,8,9]
y = [["1","2","3"],
["4","5","6"],
["7","8","9"]]
for i in range(9):
    print_board()
    if i%2 == 0:
        l = "X"
        x = int(input("X, enter a area"))
    else:
        l = "O"
        x = int(input("O, enter a area"))
    while x < 1 or x > 9 or x % 1 != 0 or u[x-1] == "O" or u[x-1] == "X":
        x = int(input("choose again"))
    u[x-1] = l
    y[(x-1)//3][(x+2)%3] = l
    if u[0] == u[1] == u[2] == l or u[3] == u[4] == u[5] == l or u[6] == u[7] == u[8] == l:
        print(l ,"win")
        print_board()
        break
    elif u[0] == u[3] == u[6] == l or u[1] == u[4] == u[7] == l or u[2] == u[5] == u[8] == l:
        print(l ,"win")
        print_board()
        break
    elif u[0] == u[4] == u[8] == l or u[2] == u[4] == u[6] == l:
        print(l ,"win")
        print_board()
        break
if i == 8:
    print_board()
    print("tie")