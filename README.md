# Know Your Plants?

A little quiz using Test Driven Development, Python and Flask.

## UX

This could form part of a website for plant identification/gardening interest, or it could be extended to be a stand-alone quiz to be played by multiple plant enthusiasts to test their knowledge!

A user should be able to have 2 attempts at each question, and then if incorrect on the 2nd attempt should be shown the correct answer. At the end of the quiz, the user is given the option to have another go, quit, or put their score onto the leaderboard.

I wanted the main feature of the quiz to be the photgraphs of the plants - which should not only be displayed clearly, but also beautifully so as to celebrate both the plants and the photography - and hopefully lead to a more pleasing UX

I wanted the photos and the questions to be displayed in the one viewport across devices, so I set the photo to take up only the top portion of the page - so there is no/minimal scrolling required to play the game even on small screens. I took a mobile-first approach to help achieve this.

 
## Features

- **Landing page**: A full-screen image and welcome jumbotron, with a start button to begin the quiz. By clicking the start button, the **Flask Session** begins and the user is directed to the first question.
- **Quiz**: The user is shown a photograph of a plant and is asked to name the plant by submitting their answer in the input. The user has 2 guesses per question, and can opt to skip to the next question after the first attempt. The user is shown flash messages: incorrect/correct/no more guesses
- **Result**: Once all quiestions have been answered the user is redirected to the results page. They will see how many questions they got right. If they scored more than half-marks they will see a "Well Done" message, if not, they will see a "Better luck next time" message. They will then be given the option to enter a username to add their score to the leaderboard (and be redirected to view it) or to quit, or start the quiz again.
- **Leaderboard**: This is a page showing the scores, highest first. When a user navigates here from the results page, their username and score will have been added. the data is stored in a txt file with a few scores hard-coded. This is because the Heroku platform does not persist the data entered. It will however, show the current users score, and any other users playing at the same time. 
The leaderboard can also be viewed at anytime by clicking the icon. However, in case the icon is clicked during a game, the leaderboard will open in a new tab to prevent the user losing their place in the quiz. 
 
### Existing Features
- At the moment, the quiz has only 5 questions. This is because it is intended largely as a demonstration of python/Flask/TDD rather than an exhaustive quiz. This could easily be extended at a later date.

## Technologies Used

- [Python](https://python.org)
- [Flask](http://flask.pocoo.org)  
    -This project uses the Flask Framework. Flask has many useful features including Flask [Session](https://pythonhosted.org/Flask-Session/) which I used to keep track of scores/question-index by storing the data on the server-side whilst the quiz is in play.


## Testing

### Automated testing
I aimed to take a test-driven approach to the development of this quiz. I used Python's [Unnitest](https://docs.python.org/2/library/unittest.html) unit testing framework. The following functions were built and tested using unnitest (the code can be found [here](https://github.com/LWilsonDev/quiz-milestone-3/blob/master/test_app.py)):
- Finding the question index from the json file
- Finding the answer from the dictionary
- Finding the images from the dictionary
- Function that takes the user's answer and compares it to the right answer

The routes, other game logic, and aspects of design and UX was tested manually.

User scenarios that were tested:

1.Question Input:
    -User enters an incorrect answer: Guess remaining goes down to 1, and an 'incorrect' message appears
    -User inputs a 2nd incorrect answer: a different error message and the correct answer is shown.
    -The user attempts to input another answer: a message saying 'you are out of guesses' is shown.
    -Tested to make sure that the user cannot score a point by entring the correct answer after 2 guesses.
    -Tested to make sure the user cannot score another point by submitting the correct answer more than once. Had to make the 'guesses remaning' count go to 0 once the correct answer was inputed.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Photos
- Cherry blossom by 'Free-Photos' [Pixabay](https://pixabay.com/en/cherry-blossom-flower-pink-blossom-1246539/)
- Apple blossom by '12019' [Pixabay](https://pixabay.com/en/apple-blossom-tree-branch-spring-173566/)
- Maple tree by 'gregovish' [Pixabay](https://pixabay.com/en/leaves-summer-green-maple-season-291024/)
- Oak tree by 'wittkielgruppe' [Pixabay](https://pixabay.com/en/oak-leaves-autumn-bokeh-green-1022074/)
- Wasabi - My own photo

### Acknowledgements

- I received inspiration for this project from https://github.com/ckz8780/ci-pp-milestone-riddlemethis