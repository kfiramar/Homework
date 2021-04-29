

def tictactoe(game):
    for i in range(3):
        if(game[i][0] == game[i][1] == game[i][2]):
            print("player " + str(game[i][0]) + " won")
            return
        if (game[0][i] == game[1][i] == game[2][i]):
            print("player " + str(game[0][i]) + " won")
            return
    if(game[0][0] == game[1][1] == game[2][2]):
        print("player " + str(game[1][1]) + " won")
        return
    if(game[2][0] == game[1][1] == game[0][2]):
        print("player " + str(game[2][0]) + " won")
        return
    print("this is a draw ")
    return



game = [[1, 2, 0],
        [2, 1, 0],
        [2, 1, 1]]
tictactoe(game)
