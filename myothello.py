# @Auther Yao Tang
# modify calculate_utility function for the game othello

from othello import *

class YaoPlayer(othello_player):
    #  This will be called once at the beginning of the game, after
    #  a few random moves have been made.  Boardstate is the initial
    #  boardstate for the game, totalTime is the total amount of time
    #  (in seconds) in the range 60-1800 that your player will get for
    #  the game.  For our tournament, I will generally set this to 300.
    #  color is one of Black or White (which are just constants defined
    #  in the othello.py file) saying what color the player will be
    #  playing.
    def initialize(self, boardstate, totalTime, color):
        print("Initializing", self.name)
        # color use for calculate utility
        self.mycolor = color
        if color == 1:
            self.opcolor = 2
        else:
            self.opcolor = 1
        # set weight for corners
        self.corners = [11,18,81,88]
        pass;
    # This should return the utility of the given boardstate.
    # It can access (but not modify) the to_move and _board fields.

    def calculate_utility(self, boardstate):
        utility = self.mycount_difference(boardstate)
        
        for i in self.corners:
            # even values of i check back one step, odd
            # values check forward one step
            if i%2 == 1:
                j = i + 1
            else:
                j = i - 1
                # if its at the top of the board go down 10 and check
                # otherwise go up 10
                if i < 80:
                    k = 10
                else:
                    k = -10
                # take the corner
                if boardstate._board[i] == self.mycolor:
                    utility = utility + 20
                else:
                    # corner taken by opponet
                    if boardstate._board[i] == self.opcolor:
                        utility = utility - 20
                    # self near corner
                    if boardstate._board[j] == self.mycolor:
                        utility = utility - 10
                    if boardstate._board[i+k] == self.mycolor:
                        utility = utility - 10
                    if boardstate._board[j+k] == self.mycolor:
                        utility = utility - 10
                # opponent near corner
                if boardstate._board[j] == self.opcolor:
                    utility = utility + 10
                if boardstate._board[i+k] == self.opcolor:
                    utility = utility + 10
                if boardstate._board[j+k] == self.opcolor:
                    utility = utility + 10
        return utility 
    def alphabeta_parameters(self, boardstate, remainingTime):
        if remainingTime > 100:
            return 4, None, None
        else:
            return 2, None, None
    def mycount_difference(self,boardstate):
        return (boardstate._board.count(self.mycolor) -
                boardstate._board.count(opponent(self.mycolor)))

def count_difference(boardstate):
    return (boardstate._board.count(boardstate.to_move)
            - boardstate._board.count(opponent(boardstate.to_move)))

play_othello(Othello(), 600, othello_player("P1"), YaoPlayer("Yao"))
##start_graphical_othello_game(othello_player("P1"), YaoPlayer("Yao"))


## To start a graphical game type:
##   start_graphical_othello_game(othello_player("Bob"), othello_player("Fred"))
## where othello_player can be replaced by MyPlayer or whatever you choose to
## call your class.

## To start a textual game (where you can have different AI players) type:
##  play_othello() will just start a default game,
##  play_othello(Othello(), 1800, MyPlayer("Name"), othello_player("Othername"))
## where MyPlayer is your class (which can have whatever name you want)
## and othello_player is just the dumb default.  You can have BobPlayer play
## FredPlayer if you define those two classes, for example.
