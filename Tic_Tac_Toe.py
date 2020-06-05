def pr_choice(status): 
    '''
    pr_choice(): start of game, take in user input of 'y' to start, and print the position helper
                if input "n", then end the program
    Input: Bool
    Output: Bool
    '''
    while status:
        print("\nYou are going to start a Tic Tac Toe game with two players!")
        start_choice = input("Are you going to start now? (Y/N)")
        if start_choice.lower() == 'y':
            print("\nThe first player is 'X', the second player is 'O'.")
            print("\nPlease indicate your move position as 1~9")
            print([1,2,3])
            print([4,5,6])
            print([7,8,9])
            break
        if start_choice.lower() == 'n':
            status = False
            break
        else:
            print("Invalid choice!")
            continue
    
    return status


def board(bd):
    '''
    board(bd): Print the current board
    Input: bd <List<List>>
    Output: None
    '''
    print("\nNow,the board looks like:")
    print(bd[0])
    print(bd[1])
    print(bd[2])

def next_move(player):
    '''
    indicate the next player, wait for input of placement
    Input: player <Str>
    Output: nxt <Str>  <- input from the user
    
    '''
    nxt = input("\nTurn of {}:  Please make the next move! (1~9)".format(player))
    return nxt

def check_move(next_move):
    '''
    check whether the input is a digit between 1 and 9
    Input: next_move <str>
    Output: False if not a valid int
            int if is a valid int
    '''
    if next_move.isdigit():
        nxt = int(next_move)
        if nxt in range(1,10):
            return nxt
        return False
    return False

def test_win(bd):
    '''
    Test whether the game comes to end: one win or full board without win
    Input: bd <List<List>>
    Output: "X" or "O" if one win
            "Draw" if game tie
            False if continue the game
    '''
    #Check one row win
    for row in [0,1,2]:
        if bd[row][0]== bd[row][1] and bd[row][0]== bd[row][2] and bd[row][0] in ["X","O"]:
            return bd[row][0]
    
    #Check one col win
    for col in [0,1,2]:
        if bd[0][col]== bd[1][col] and bd[0][col]== bd[2][col] and bd[0][col] in ["X","O"]:
            return bd[0][col]
    
    #Check one diagonal win
    if bd[0][0] in ["X","O"] and bd[0][0] == bd[1][1] and bd[0][0] == bd[2][2]:
        return bd[0][0]
    
    elif bd[0][2] in ["X","O"] and bd[0][2] == bd[1][1] and bd[0][2] == bd[2][0]:
        return bd[0][2]
    
    #Check full board
    else:
        for r in range(0,3):
            for c in range(0,3):
                if bd[r][c] not in ["X","O"]:
                    return False
        
        return "Draw"

def cvt_pos(next_move):
    '''
    convert user input(1-9) to a list indicate the position in board
    Input: int
    Output: List<int>
    '''
    return [int((next_move-1)/3),(next_move-1)%3]

def rej(bd,pos):
    '''
    put the input into board, or if occupied, reject the input
    Input: the board, the postion to put, the current player
    Output: True if not occupied
            False if occupied
    
    '''
    if bd[pos[0]][pos[1]] in ["X","O"]:
        return False
    return True
    
def put(bd,pos,player):
    '''
    put the player's input into pos
    Input: bd<List<List>>, pos<List>, player <str>
    Output: bd<List<List>>
    '''
    bd[pos[0]][pos[1]] = player
    return bd

def swap_player(player):
    '''
    swap the player
    Input: "X" or "O"
    Output: "O" or "X"
    '''
    if player == "X":
        player = "O"
    else:
        player = "X"
    return player

def again():
    '''
    Ask user whether to start the game again
    Input: None
    Output: Bool
    '''
    start_choice = input("\n\nDo you want to start the game again?(Y/N)")
    if start_choice.lower() == 'y':
        return True
    return False      

#Game Starts Here:

status = True
##Initialise the board
#Grab user input -> Start Game or not
status = pr_choice(status)

while status:    

    #If start, Create a new board, and print it
    bd = [[" "," "," "],[" "," "," "],[" "," "," "]]
    board(bd)

    #Set the first player
    player = "X"


    ##Process the game

    #check whether the game ends
    while not test_win(bd):#the game goes on

        #Grab user's input as int
        nxt = next_move(player)

        #if the input is not a valid int, print warning and process it again     
        if not check_move(nxt):
            print("It's not a valid input!\n")
            continue

        #if the input is valid as nxt(int)
        #convert the int pos to grid pos
        pos = cvt_pos(check_move(nxt))

        #if the position is occupied, print warning and process it again
        if not rej(bd,pos):
            print("It's occupied!\n")
            continue

        #if the pos is not occupied,update the board, and print it
        bd = put(bd,pos,player)
        board(bd)
        
        #shift to next player
        player = swap_player(player)
     

    #jumps out of loop means the game ends
    if test_win(bd)=="Draw":#nobody wins
        print("\nDraw!")

    else:
        print("\n{} win!".format(swap_player(player)))
        
    #ask user play again or not
    status = again()
