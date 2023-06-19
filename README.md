 
# Pong_Game
This Python code creates popular Pong game using python in-built turtle module  

This is a simple implementation of the classic Pong game using Python and the Turtle graphics library.
We can breakdown the logic of the game into :
- Creating the screen
- Create and move the paddle
- Create another paddle so that we can have a two player game
- Create the ball and make it move
- Detect collision with the wall and make it bounce back
- Detect collision with the paddle 
- Detect when paddle misses the ball
- keep a record of score 


GAME DESCRIPTION :
- Pong is a two-player game where each player controls a paddle. 
- The goal is to use the paddles to hit the ball and prevent it from crossing your side of the screen. 
- Players earn points when the opponent fails to return the ball.

HOW TO PLAY THE GAME :
1. Run the `pong_game.py` file to start the game.
2. Player 1 controls the right paddle using the 'Up' and 'Down' arrow keys.
3. Player 2 controls the left paddle using the 'W' and 'S' keys.
4. The game continues until one player reaches the winning score (default is 5).
5. The ball speed increases each time it bounces off a paddle.
6. Press 'Esc' to quit the game at any time.

Files :
- `pong_game.py`: The main script that initializes the game, sets up the screen, and handles the game loop.
- `paddle.py`: Contains the `Paddle` class responsible for creating and managing the paddles.
- `ball.py`: Contains the `Ball` class responsible for creating and managing the ball.
- `scoreboard.py`: Contains the `Scoreboard` class responsible for keeping track of and displaying the scores.

Enjoy the game!!!
