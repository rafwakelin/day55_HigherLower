# Imports
from flask import Flask
from random import randint

# Creates the server
app = Flask(__name__)

# Generates a random number
number = randint(0, 9)


# Creates the initial page
@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/PnTro4KtzGQDDlGrZB/giphy.gif'>"


# Creates response page and compares user number against the random
@app.route(f'/<int:user_guess>')
def compare(user_guess):
    if user_guess > number:
        return "<h1>That's too high!</h1>" \
               "<img src='https://media.giphy.com/media/uEgup6iJqTLeMSvcHw/giphy.gif'>"
    elif user_guess < number:
        return "<h1>Too Low!</h1>" \
               "<img src='https://media.giphy.com/media/pzFsTwKRGB0NVfjEeZ/giphy.gif'>"

    else:
        return "<h1>Nailed it!!!<h1>" \
               "<img src='https://media.giphy.com/media/ejJclNX60XyEo555wW/giphy.gif'>"


# Runs the server using the IDE GUI
if __name__ == "__main__":
    app.run(debug=True)
