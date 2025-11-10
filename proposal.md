Title: Driving Minigame

Repository: https://github.com/erinfte/driving-game.git

Description: This pygame will have the player drive a car and avoid oncoming traffic. The player plays to reach their high score, and if the player collides with another vehicle, the player loses the game.

Features:

Driving: The player will control one object, and this object will be able to move vertically to avoid objects. I will use rect to update the players position based on key inputs.

Vehicles: Opposing vehicles will be generated randomly on the right screen and move towards the left, similar to the rain mechanics we created. If the player collides with them, then the game will end.


Challenges:
I don’t think I’ve gotten to work with player commands in pygame, so I’ll have to implement them. Most likely just WASD keyboard commands.
I need to make collision with the object become a game over. I have to think about how I could trigger that collider.
I need to create a timer that will display the time score at the end of the game.
If I wanted to make it more challenging, I could make the speed of other vehicles increase as time progresses.
I also need to optimize my game to run without slowing down, so that the game is playable.

Outcomes:
My ideal outcome is a driving minigame that implements the features listed, and optimized well enough to run smoothly. I want to make sure I am using the right PEP8 structures in my code and keeping the code clean and understandable.

The minimal viable outcome would be the base driving game that runs without repeating too many processes every frame. I wouldn’t need to implement the high score or the speed increase as time progresses. If it came down to it, I would just want the driving and colliding to work, and I could cheap out on assets if it got rough.

Milestone 1: 11/17/25 This is when I submit the rough code. I don't expect everything to be created, but maybe the player can move, and the other cars also move.
Milestone 2: 11/24/25 This is when I will work on the collision and make the player able to interact with the other cars.
Milestone 3: 12/01/25 This is where I add the timer, fix up the assets, and optimize the code.
Milestone 4: 12/07/25 This is the final submission where I check to make sure the game runs properly and maybe make it a bit more polished
