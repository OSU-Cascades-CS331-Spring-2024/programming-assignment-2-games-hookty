[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/i3cjXgnP)
# othello-python
Starter Code for Othello AI Agent Programming Assignment

Originally created by Erich Kramer at OSU for Professor Rebecca Hutchinson. Cleaned up by Rob Churchill.

How to play a game:

1. Run `python3 game_driver.py [player_type] [player_type]`.
2. Choose `human`, or `minimax` as the player types.
3. Follow the prompts to choose where to place stones.

    python3 game_driver.py minimax minimax

# INSTRUCTIONS

## Problem Statement
 In this assignment, we will be playing a classic two-player game, Othello! Your job is to create an agent that uses the minimax algorithm to find the next move that your agent should make. You can find starter code for this assignment in the GitHub Classroom repository. For this and every assignment, you must implement your solution using only the standard libraries that Python3 provides. If you want to use external libraries, please ask me first.

 You may use any version of Python3 that suits you, but I will use Python 3.11 for grading. Othello is generally played on an 8x8 board, but for this assignment, we will be considering a 4x4 board. Your solution must work on an Othello board of any size (we can assume that it is square). You will calculate the next move for the computer player using the Minimax algorithm. Since we will be using ASCII art to display the board, we will use the symbols X (for the dark player who goes first) and O (for the light player who goes second). We will operate under the assumption that the player going first is the maximizing player and the player going second is the minimizing player.

 The command line allows you to select whether a player is a human player or a computer player.
 Your assignment will only be graded with the human player moving first and the Minimax player
 moving second. Note that the 4x4 game of Othello is asymmetric; the player moving second has
 a serious advantage over the player moving first. In this assignment, the computer player, when
 going second, should always either win or tie.

## Implementation Requirements:

### Utility function:
 The 4x4 version of Othello is small enough that we can generate the entire game tree while doing the Minimax search. As a result, you do not need to create an evaluation function for non-terminal nodes. You will, however, need to create a utility function that determines the "goodness" of a terminal state. You will need to create this utility function on your own. When creating the utility function, remember that the player that moves first is assumed to be the maximizing player. Successor function: You will also need to create a successor function. This function takes the current state of the game and generates all the successors that can be reached within one move of the current state.

### Minimax function: 
 You will need to implement the Minimax-Decision, Max-Value and Min-Value functions on that slide. You should be sure to include a depth parameter to ensure that your minimax player will make a decision in a timely manner (less than two seconds), regardless of the board size. You will need to come up with a heuristic evaluation function to apply when you hit the depth limit in your search. You will need to override the default get_move function of the Player class for the MinimaxPlayer class in order to produce an action using Minimax.

In addition to the functionality described above, you may need to implement some other code to do things like bookkeeping.

## Analysis Requirements:

 Add in a few lines of code to allow you to keep track of the time it takes the minimax player to make move. At the end of each game, print out the average time per move that the minimax player takes.

 For the questions below, write your answers in a plaintext file called README. If at any point in these experiments, the minimax player takes more than ten seconds to make a move, you should terminate the process and report in your README that the minimax player was not able to make a move quickly.

### 1. Simulate four games between yourself and the minimax player on a 4x4 board, with the depth parameter set to 5, 3, 2, and 1, respectively.

 a. What were the results of each game?

 b. Did the minimax player’s moves change when the depth was limited to smaller
 
 and smaller values?

 c. What was the average time per move for each of the games? Comment on why there is or is not a difference.

### 2. Simulate two games between yourself and the minimax player on an 8x8 board, with the depth parameter set to 5 and 2.

 a. What were the results of each game?

 b. Did the minimax player’s moves change when the depth changed?

 c. What was the average time per move for each of the games? Comment on why there is or is not a difference.

## Deliverables:
 You should submit everything below to your GitHub classroom repository:
 https://classroom.github.com/a/i3cjXgnP
 1. READMEFile
 2. Python code

 ### Citations:

i fed chatgpt this readme as context, along with my workspace, annd it returned:

[the AI is coming for u jorb](exploration.png)