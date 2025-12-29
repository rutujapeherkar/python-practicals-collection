
print("Tic Tac Toe Game")

list = [1,2,3,4,5,6,7,8,9]

def show_board():
    for i in list:
        print(i, end='\t')
        if i % 3 == 0:
            print(end='\n')


i = 0
while i<=2:
    show_board()
    print("Player - 1, please enter your choice : ", end = '')
    p1 = int(input())
    for i in list:
        if i == 'x' or i == 'o':
            print("Block is already occupied. pLease repeat your turn")
        elif i == p1:
            list[i] = 'x'

        if list[0] == 'x' and list[1] == 'x' and list[2] == 'x':
            print("Player -1 wins ")
            break

        if list[3] == 'x' and list[4] == 'x' and list[5] == 'x':
            print("Player -1 wins ")
            break

        if list[6] == 'x' and list[7] == 'x' and list[8] == 'x':
            print("Player -1 wins ")
            break

        if list[0] == 'x' and list[4] == 'x' and list[8] == 'x':
            print("Player -1 wins ")
            break

        if list[2] == 'x' and list[4] == 'x' and list[6] == 'x':
            print("Player -1 wins ")
            break

        if list[0] == 'x' and list[1] == 'x' and list[2] == 'x':
            print("Player -1 wins ")
            break

    print("Player - 2, please enter your choice :", end= " ")
    p2 = int(input())

    for i in list:
        if list[i] == 'x' or list[i] == 'o':
            print("Block is already occupied. pLease repeat your turn")
        elif list[i] == p2:
            list[i] = 'o'

        if list[0] == 'o' and list[1] == 'o' and list[2] == 'o':
            print("Player - 2 wins ")
            break

        if list[3] == 'o' and list[4] == 'o' and list[5] == 'o':
            print("Player - 2 wins ")
            break

        if list[6] == 'o' and list[7] == 'o' and list[8] == 'o':
            print("Player - 2 wins ")
            break

        if list[0] == 'o' and list[4] == 'o' and list[8] == 'o':
            print("Player - 2 wins ")
            break

        if list[2] == 'o' and list[4] == 'o' and list[6] == 'o':
            print("Player - 2 wins ")
            break

        if list[0] == 'o' and list[1] == 'o' and list[2] == 'o':
            print("Player - 2 wins ")
            break