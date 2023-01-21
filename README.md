# DungeonTextGame

### Video of Code Running:
https://drive.google.com/file/d/11sI5JmzCxGBWQswa5orF-q3LjHwl2yOA/view?usp=share_link

## Function:
This project is a fantasy dungeon exploration text based game made in python. The game has the player trying to progress through this dungeon whihc is meant to be a prison for the player. The code provides the player with many choices to choose from like which door do they want to go through or which weapon they want with some hidden easter eggs like when certain names are put into the game or when certain commands are issued at certain areas of the game. To find these secret commands and easter eggs, it would be near impossible for a normal person meaning the players have to check the actual source code of the game to find out what they are because there were many games I played where quests or areas were only discovered by looking at the games code and I looked that aspect a lot of it being completely hidden and only being revealed only to the most dedicated players who even go as far as checking the code of the game so I wanted to put that in my game. But at its core, this game is a choose your own adventure sort of text game where each choice the player makes will impact the story and change the game so the game will have many paths based on how you play the game so try to discover them all ;)

## Purpose:
This game is just a fun game for myself to play and to show to my friends and family and for them to play it. It's also for anyone who wants to play a fun quick game online and who wants to play a fun and small fatasy game that I will try to update with more features and levels. the reason I made this project was because I wanted to improve my general ability and familiarity with Python meaning I wanted to imrpove my ability to problem solve and just my general understanding of Python like when to use certain code.

## Something New I learned:
Something new that I learned from this project is how to use the time.sleep function which allows me to delay certain pieces of code to appear after a wait like 5 seconds to help space out my code when I presented text to the player so that they don't get overwhelmed which was done using time.sleep() as by delaying the appearance of certain parts of code, it made it more easy to digest for the player who had to read it all by providing them with hime to read the text on the screen. I was also helped by my coding instructor, Mr. Bowman, who helped me understand classes and their function in code and how they help make code easier to read and simpler to understand by placing all the code that relates to the player in one place for easy access in 1 place.
##### Examples:
##### Example of time.sleep():
<img width="1268" alt="Screenshot 2023-01-21 at 2 41 03 AM" src="https://user-images.githubusercontent.com/97945763/213824211-fd154a48-04e0-4620-9b39-f18557798085.png">
Here's an example of where I used time.sleep() to provide the player where time.sleep() to be able to read the introduction scene which described to them where they were so that they wouldn't miss anything important that they had to know
##### Example of Class and Objects:
![Screenshot 2023-01-21 at 5 00 34 AM](https://user-images.githubusercontent.com/97945763/213836689-e985d432-6902-4e22-9bb2-a93e34dbaf69.png)
Here's an example of my class and objects in the class where I placed all the functions that relate to the player in the class so that the functions and code are easy to find throughout my whole code.

## Solving a Problem:
One example of me solving a problem in my code is when I was trying to implement my class and objects into my main function and code as I had to assign the class to a variable to use the objects in it but what I did was that I made that variable for the class twice, one for when the player chose the weapon and once more when the player chose their divine artifact but the problem with that was that because I made that variable twice(meaning I had the same line of code attaching the class to a variable in both cases), for some reason all the players data stored in the class was deleted which confused me till I realized that the reason all the players data in the class like their name, weapon, and etc. was beign deleted was because I was making a variable twice for the class to attach it to my code, When I made the variable a second variable, it was reseting all the players data when I made it again meaning all I had to do was erase the second time I made a variable for it and then my code worked again as the class and objects were implemented and the players data stopped being reset.
<img width="1024" alt="Screenshot 2023-01-21 at 5 05 17 AM" src="https://user-images.githubusercontent.com/97945763/213837740-d60b46cc-8683-4518-86bb-3f9dadc92322.png">

## Data Abstraction:
Data abstraction in my code can be seen when certain data is stored like in a variable or array(when there were multiple "correct" choices or possible choices) where and where that data is then retrieved later on by different code statements like conditional statements. This can be seen when I created arrays in my code like when I made an array with all the possible weapon choices and if the weapon the player chose was in that array, than whatever weapon they chose would be set as their weapon and stored in the player class under the object of their equipped weapon but this data isn't just left there but it's then used later on and retrieved by conditional statements like when the player is crafting a new item by combining their weapon and divine artifact where if statements check what weapon they have to list the possible crafted items they can make. If I didn't use data abstraction in my code/program, it wouldn't work because the players weapon wouldn't be stored anywhere meaning that no matter what weapon they chose, it wouldn't matter because the code would not store it anywhere meaning that it wouldn't be able to check which weapon they have and wouldn't be able to list specific crafted weapons based on their weapons as the weapon they chose isn't stored anywhere. Using things like arrays also helped my code be less repetitive as I didn't have to write the same code over and over for each weapn to be set as the players equipped weapon but I could just write the same code once for the players weapon choice to be set as their weapon and have it apply to all the chosen weapons in the array.
#### Where the array with the weapon choices are:
<img width="1300" alt="Screenshot 2023-01-21 at 5 27 51 AM" src="https://user-images.githubusercontent.com/97945763/213839921-212a6f99-55df-4154-88e7-19dd5a78f1af.png">
#### Where the weapon they chose is set as their weapon:
<img width="1088" alt="Screenshot 2023-01-21 at 5 28 18 AM" src="https://user-images.githubusercontent.com/97945763/213839927-a6e6aab6-d5e9-4562-91f1-b7c6e6fe1ccd.png">

## Procedural Abstraction:
### Procedure:
An example of procedure in my code is when my code takes an argument like when asking the player what weapon they want or what their name is as those are stored in their own variables(weapon_chosen for the players weapon and name for the players name) which the data stored in those variables is used by another function like the stats function in the class for the player when printing the players stats like their current weapon, their name, and etc. This can also be seen when I ask the player for their weapon choice and that data is again stored in a variable which is used by another function like the one that provides the player with the choices of crafted items based on what weapon they chose.
#### When I ask the player for a weapon choice:
<img width="1119" alt="Screenshot 2023-01-21 at 5 40 44 AM" src="https://user-images.githubusercontent.com/97945763/213840291-8b469cbc-1d97-4074-8506-9a1312d3e7f6.png">
#### When I ask the player for their name:
<img width="1044" alt="Screenshot 2023-01-21 at 5 42 36 AM" src="https://user-images.githubusercontent.com/97945763/213840359-747592af-0559-4ea3-8ee6-40d3bb4b81af.png">
#### Where that data is used in the function:
<img width="690" alt="Screenshot 2023-01-21 at 5 39 53 AM" src="https://user-images.githubusercontent.com/97945763/213840268-c9564558-c92e-4326-a8bf-469515f8f816.png">
#### Where the list of crafted items based on chosen weapon:(example)
<img width="1268" alt="Screenshot 2023-01-21 at 5 43 45 AM" src="https://user-images.githubusercontent.com/97945763/213840401-c46ad7dd-e4c8-4698-99eb-a27988f2f36c.png">

### Algorithm:
Algorithm can be seen in my code through sequencing, selection, and iteration:

#### Sequencing:
Sequencing can be seen in my code as the way the computer reads the code is from top to bottom meaning that if lets say I mention a function in my main function(if __name__ == "__main__"), than that function needs to be above the main function as due to the computer reading the code from top to bottom, the functions mentioned in the main function have to be mentioned above the main function as then, the code already knows what to do when those functions are mentioned in the main function as the code already read through that function at the top of the code. This can be seen when I mention the function where an administrator confronts you in the main function so I have to mention the function for this confrontation above the main function so the code knows what to do when we reach where this function is called. Meaning that my code is more simple and easy to read as everything is placed in order with functions mentioned in the main function being above the main function so they can be called when they are used in the main function.
##### Where the function for the confrontation is:
<img width="998" alt="Screenshot 2023-01-21 at 5 51 27 AM" src="https://user-images.githubusercontent.com/97945763/213840615-692bd604-d787-4b6e-bdf2-e2e276f1261a.png">
##### Where the confrontation function is called:
<img width="811" alt="Screenshot 2023-01-21 at 5 51 47 AM" src="https://user-images.githubusercontent.com/97945763/213840627-a3406b3e-f1cf-4e92-a06a-33dbcce2f7e8.png">

#### Selection:
Selection can be seen repeatedly throughout my code like in while loops and if statements, which ar ejust conditional statements, as those statements have to be selected if the condition for them is met. This can be seen with my if statements like when the player's name is asked for and set, there are if statements which are called based on the players name if the players name is the same as the one stated in the if statements condition which is like specific names. and if the players name doesn't fit any of those conditions, than the code doesn't call that if statement and just skips it as the condition isn't met to call that code.
#### If statements based off of name:
<img width="1306" alt="Screenshot 2023-01-21 at 5 59 41 AM" src="https://user-images.githubusercontent.com/97945763/213840839-aa013ec6-fd93-4113-aa3f-573a15d33107.png">

#### Iteration:
Finally, iteration can be seen in my code as iteration is when code is called upon and ran over and over when the condition stated is met which causes the code to repeat over and over infinitely or until the code is repeated a certain amount of times if stated. This can be seen when I used a while loop which had the condition be set to as long as the while loop was True which in my code was always the case meaning the code would keep on repeating forever as long as the code was True which was always the case which was important like when I used continue to cause the code to repeat as continue skipped the current run of the code the player is in(meaning it skipped the rest of the code in the run it was in) and went to the next run of the code(meaning the code restarted meaning the game was restarted) but the code would be exited meaning it would stop being iterated when sys.exit() was used as that meant the player wanted to exit the code(game) meaning the condition for the code(which was being true) wasn't being met anymore(it became false).
##### While Loop:
<img width="617" alt="Screenshot 2023-01-21 at 6 05 15 AM" src="https://user-images.githubusercontent.com/97945763/213840973-d35cff24-7dbe-4cb5-a495-d873986f66fa.png">
##### Example of sys.exit() to exit the code:
<img width="1274" alt="Screenshot 2023-01-21 at 6 05 54 AM" src="https://user-images.githubusercontent.com/97945763/213840992-b3c87ab0-8b23-4abd-9c06-7a336135d76c.png">

#### Overall:
Procedural abstraction helped my code be less complex overall because with it, all my code was organised based on order of use from top to bottom meaning code used by a function was placed above that function ensuring that my code was in the proper placement and that it continued to work which by usingthese functions, it also helped make my code less repetitive as if I used certain code multiple times, by using a function, I didn't have to repeat that code over and over each time that code was needed, but instead, I could just mention that function which already has that code stated.
