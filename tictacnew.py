#Swagatam Bera
#Encryptix Artificial Intelligence-TicTacToe
import sys

dicti = {1: ' ', 2: ' ', 3: ' ',
          4: ' ', 5: ' ', 6: ' ',
            7: ' ', 8: ' ', 9: ' '}
def printtic(dicti):
    print(dicti.get(1), "|", dicti.get(2), "|", dicti.get(3))
    print("----------")
    print(dicti.get(4), "|", dicti.get(5), "|", dicti.get(6))
    print("----------")
    print(dicti.get(7), "|", dicti.get(8), "|", dicti.get(9))

def insert(inp, letter):
    if conditionfordraw():
        print("It is a draw")
        sys.exit(0)
    if dicti.get(inp) != ' ':
        print("Already occupied, try again!")
        movebyplayer()
        return
    dicti[inp] = letter
    printtic(dicti)
    if conditionforwin():
        if letter == player:
            print("Player won the game")
        else:
            print("Computer has won the game")
        sys.exit(0)

def conditionfordraw():
    for value in dicti.values():
        if value == ' ':
            return False
    return True

def conditionforwin():
    win_conditions = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  
        (1, 5, 9), (3, 5, 7)              
    ]
    for a, b, c in win_conditions:
        if dicti[a] == dicti[b] == dicti[c] and dicti[a] != ' ':
            return True
    return False

def movebyplayer():
    inp = int(input("Enter the position (1-9): "))
    insert(inp, player)

def minimaxalgo(dicti, depth, is_maximizing):
    if conditionforwin():
        return 1 if not is_maximizing else -1

    if is_maximizing:
        best_score = -float('inf')
        for i in range(1, 10):
            if dicti[i] == ' ':
                dicti[i] = computer
                score = minimaxalgo(dicti, depth + 1, False)
                dicti[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(1, 10):
            if dicti[i] == ' ':
                dicti[i] = player
                score = minimaxalgo(dicti, depth + 1, True)
                dicti[i] = ' '
                best_score = min(score, best_score)
        return best_score

def movebycomputer():
    best_score = -float('inf')
    best_move = 0
    for i in range(1, 10):
        if dicti[i] == ' ':
            dicti[i] = computer
            score = minimaxalgo(dicti, 0, False)
            dicti[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    insert(best_move, computer)


player = 'O'
computer = 'X'
printtic(dicti)
print("Computer starts with:")
movebycomputer()

while True:
    if conditionfordraw():
        print("Its a draw")
        sys.exit(0)
    movebyplayer()
    movebycomputer()
    print("______________________________________________")
