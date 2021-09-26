"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0
    for i, row in enumerate(board):
        for j, mark in enumerate(row):
            if mark:
                count = count + 1

    if count % 2 == 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i, row in enumerate(board):
        for j, mark in enumerate(row):
            if not mark:
                actions.add((i, j))
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]]:
        raise NameError("action not allowed")

    board_copy = copy.deepcopy(board)
    board_copy[action[0]][action[1]] = player(board)

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Deepcopy the board
    board_copy = copy.deepcopy(board)
    
    # Check the lines and columns
    for direction in range(2):
        for player in [X, O]:
            for row in board_copy:
                if row == [player, player, player]:
                    return player
        # Transpose list to check columns
        board_copy = list(map(list, zip(*board_copy)))

    # Check the diagonals
    for j in range(2):
        count_X = 0
        count_O = 0
        for i in range(3):
            if board_copy[i][i] == X:
                count_X += 1
                if count_X == 3:
                    return X
            elif board_copy[i][i] == O:
                count_O += 1
                if count_O == 3:
                    return O
        board_copy.reverse()

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True

    # If it's a tie
    count = 0
    for row in board:
        for mark in row:
            if mark:
                count += 1 

    if count == 9:
        return True

    # If the game is not over, return False
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def maxvalue(board):
    v = -2
    # If terminal state, evaluate the board
    if terminal(board):
        return utility(board)

    #If not a terminal state, find possible actions
    for action in actions(board):
        v = max(v, minvalue(result(board, action)))
        return v

def minvalue(board):
    v = 2
    # If terminal state, evaluate the board
    if terminal(board):
        return utility(board)

    #If not a terminal state, find possible actions
    for action in actions(board):
        v = min(v, maxvalue(result(board, action)))
        return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    # The maximizing player picks action a in Actions(s) that produces the highest value of Min-Value(Result(s, a)).
    if player(board) == X:
        v_max = -2
        for action in actions(board): 
            score = maxvalue(result(board, action))
            if score > v_max:        # if the score is bigger than the best score so far
                v_max = score        # update best score
                best_action = action # save the action
            if score == 1:
                break
        return best_action

    # The minimizing player picks action a in Actions(s) that produces the lowest value of Max-Value(Result(s, a)).
    elif player(board) == O:
        v_min = 2
        for action in actions(board): 
            score = minvalue(result(board, action))
            if score < v_min:        # if the score is smaller than the best score so far
                v_min = score        # update best score
                best_action = action # save the action
            if score == -1:
                break
        return best_action

            

    





    



    