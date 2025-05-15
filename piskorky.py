# project tic-tac-toe:
# create a tic-tac-toe game such that:
# 1. player 1 and 2 take turns, the game always prompts player 1 or 2 to make their move, player 1 enters the value "X" and player 2 enters the value "0"
# 2. the game displays the current round, the current state of the game board, the coordinates of the x and y axes are in the range from 0 to 2
# 3. use a 2D array (array of arrays) to fill in the values
# 4. during a turn, the game asks the player for the coordinates, which they enter via the keyboard
# 5. implement error handling
# 6. the game displays the winner in case of a win, as well as a draw
# 7. after the game ends, create an option to repeat the game from the beginning or to quit


x = 1
stlpce = 3
riadky = 3
x = 2
y = 2
n = str("")
p = ""
hrac = 1

pole = list([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])
antipole = list([[[0, 0], [0, 1], [0, 2]], [[1, 0], [1, 1], [1, 2]], [[2, 0], [2, 1], [2, 2]], [[0, 0], [1, 0], [2, 0]], [[0, 1], [1, 1], [2, 1]], [[0, 2], [1, 2], [2, 2]], [[0, 0], [1, 1], [2, 2]], [[0, 2], [1, 1], [2, 0]]])

# zobrazenie tabulky
def tabulka(pole):
	print(" ", end="")
	for hlavicka in range(0, stlpce):
	    print("", hlavicka, end="")
	print()
	for stlp in range(0, stlpce):
	    print(stlp, end=" ")
	    for riad in range(0, riadky):
	        print(pole[stlp][riad], "", end="")
	    print()

# zadavanie hodnot aj s opravou chyby
def vstup(x, y):
    pokracuj = True
    while pokracuj:
        while True:
            try:
                x = int(input('enter row:'))
            
                while x not in range(0, riadky):
                    print("value is out of range")
                    x = int(input("enter the correct row:"))
                else:
                    break
            except ValueError:
                print("incorrect value")
        while True:        
            try:
                y = int(input('enter column:'))
            
                while y not in range(0, stlpce):
                    print("value is out of range")
                    y = int(input("enter the correct column:"))
                else:
                    break
            except ValueError:
                print("incorrect value")
        if pole[x][y] == '0' or pole[x][y] == 'X':
            print("the place is already taken, try another one")
        else:
            pokracuj = False

    return(x, y)

# zistenie vytazstva
def vyhra(p):
    w = len(antipole)
    for q in range(w):
        m = str("")
        #print(antipole[q], end=" ")
        for n in range(3):
            s, d = antipole[q][n]
            m = m + pole[s][d]
            #print(pole[s][d], end="")
        #print(m, end="")
            if m == "XXX":
                p = "Player 1 won"
                break
            elif m == "000":
                p = "Player 2 won"
                break
            else:
                p = "no one has won yet"
            #print()
        if m == "XXX" or m == "000":
            break
    return(p)

        
w = len(antipole)
for q in range(w):
    #print(antipole[q], end=" ")
    for n in range(3):
        s, d = antipole[q][n]
        #print(pole[s][d], end="")
    print()
# prevodnik = list(vstup(x, y))       # prepisujem hodnoty x a y z funkcie, aby som nemusel pouzit globalnu funkciu 
                                    #a aby mi tieto hodnoty zostali zachovanie, aby sa znova vsade nepocitalo s predvolenymi hodnotami x, y

print("""Good day,
this is the game Tic-Tac-Toe.
Player 1 starts and enters the value X,
Player 2 enters the value 0,
the first one to achieve three identical
values in a row, diagonally,
or vertically, wins.
If neither achieves this,
after the 9th round it's a draw.""")
while True:
    hrac = 1
    kolo = 1
    hrac_prirastok = 0
    pole = list([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])
    while True:
        n = (vyhra(p))
        if n == "Player 1 won" or  n == "Player 2 won":
            print("Congratulations on your victory, player:", hrac)
            break
        print(n)
        if kolo == 10:
            print("no one won, try again")
            break
        hrac = hrac + hrac_prirastok
        print("round number:", kolo)
        print("Turn of player: ", hrac)
        print(tabulka(pole))
        prevodnik = list(vstup(x, y))
        c, d = prevodnik
    
        kolo += +1
        if hrac == 1:
            pole[c][d] = 'X'
            hrac_prirastok = 1
        else:
            pole[c][d] = '0'
            hrac_prirastok = -1
    print("If you want replay game again, press 1")
    print("To exit the game, press anything else.")
    try:
        opakuj_hru = int(input('zadaj:'))
        if opakuj_hru == 1:
            print("new game")
        elif opakuj_hru != 1:
            print("The end")
            break
    except ValueError:
            print("The end")
            break
# print(prevodnik[0])
# print(prevodnik[1])  

# print(tabulka(pole))
# c, d = prevodnik
# print("hodnota je: ", c, d)
# print(vyhra(p))