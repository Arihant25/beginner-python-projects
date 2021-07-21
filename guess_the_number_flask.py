from flask import Flask
from random import randint

# Create an instance of Flask class
app = Flask(__name__)

# GIF Links
INTRO = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"
HIGH = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
LOW = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
CORRECT = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"

# Choose a random number
correct_answer: int = randint(0, 9)


@app.route('/')
def index() -> str:
    return f'''
    <h1>Welcome to Guess the Number!</h1>
    <p>Guess a number from 0 to 9 by appending the number to the end of the URL.</p>
    <img src="{INTRO}">
    '''


@app.route('/<int:num>')
def guess(num) -> str:
    if num == correct_answer:
        return f'''
        <h1>Correct!</h1>
        <img src="{CORRECT}">
        '''
    elif num < correct_answer:
        return f'''
        <h1>Too low!</h1>
        <img src="{LOW}">
        '''
    else:
        return f'''
        <h1>Too high!</h1>
        <img src="{HIGH}">
        '''


if __name__ == '__main__':
    app.run()
