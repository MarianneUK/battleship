# WHERE'S THE SHIP?

Where's the Ship? is a simple guessing game based on the classic game "Battleships". Deployed to Heroku, this mini-game is python based and single player.

[View the live project here.](https://wheres-the-ship.herokuapp.com/)

![readme hero image](/assets/images/webpage.png)

# Table of Contents
- [1. How to Play](#how-to-play)
- [2. Features](#features)
  * [2.1. Existing Features](#existing-features)
  * [2.2. Features Left to Implement](#features-to-implement)
- [3. Testing](#testing)
  * [3.1. Bugs](#bugs)
  * [3.2. Validator Testing](#validator-testing)
- [4. Deployment](#deployment)
- [5. Credits](#credits)

<a name="how-to-play"></a>
# 1. How to Play
  [Go to the top](#table-of-contents)


 Where's the Ship? is based on the classic pen-and-paper game Battleships. You can read more about it on this [Wikipedia page](https://en.wikipedia.org/wiki/Battleship_%28game%29). 
 In this single-player version, the player is asked for their name and a board is automatically generated. The board's spaces are marked with " . " and the shots are marked with " X ".
 The player has 5 turns to guess where the ship is. After 5 attemps, the game is over.

<a name="features"></a>
# 2. Features
  [Go to the top](#table-of-contents)

  The project is built in Python but can be easily accessed on a web page, thanks to Code Institute's mock terminal for Heroku.

  ![homepage](/assets/images/homepage.png)

<a name="existing-features"></a>
## 2.1. Existing Features
  [Go to the top](#table-of-contents)

  - Random board generation
  - Random ship placement
  - Accepts user input

![feature image](/assets/images/feat1.png)

  - Input validation
     + the player cannot enter coordinates outside the grid
     + the player cannot enter the same coordinates twice

![feature image](/assets/images/feat2.png)

<a name="features-to-implement"></a>
## 2.2. Features Left to Implement
  [Go to the top](#table-of-contents)

  - more ships and bigger grid
  - two player mode against the computer
  - option for the user to choose the grid size and the number of ships

<a name="testing"></a>
# 3. Testing
  [Go to the top](#table-of-contents)

  This project was manually tested by doing the following:
   - passed the code through a PEP8 test
   - entered invalid input to test error messages
   - the project was tested on different terminals

<a name="bugs"></a>
## 3.1. Bugs
  [Go to the top](#table-of-contents)

### 3.1.1. Known bugs
  - Issues met were related to the user's turns display not displaying digits.
  - Game over message not displaying after 5 turns.

### 3.1.2. Solved bugs
  - Both above bugs were resolved.

### 3.1.3. Remaining bugs
  - Error messages from GitPod and the PEP8 validator.

<a name="validator-testing"></a>
## 3.2. Validator Testing
  [Go to the top](#table-of-contents)
  
  - PEP8
    + These are the errors returned from PEP8online.com

![pep8 image](/assets/images/pep8.png)

<a name="deployment"></a>
# 4. Deployment
  [Go to the top](#table-of-contents)

 This project as deployed using Code Institute's mock terminal for Heroku.
  - Steps for deployment:
    + Fork or clone this repository
    + Create a new Heroku app
    + Set the buildbacks to <Python> and <NodeJS> in that order
    + Link the Heroku app to the repository
    + Click on **Deploy**

<a name="credits"></a>
# 5. Credits
  [Go to the top](#table-of-contents)

  - Code Institute for the deployment terminal
  - Source code and tutorials on GitHub, Trinket, PythonDex, RtoDto and Youtube.

