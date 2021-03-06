"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def play_game():
    
    play = request.args.get("yn")
    if play == "yes":
        return render_template("game.html")
    else:
        return render_template("goodby.html")


@app.route('/madlibs')
def show_madlib():
    
    noun = request.args.get("noun")
    adjective  = request.args.get("adjective")
    color =  request.args.get("color")
    person =  request.args.get("person")
    gender =  request.args.get("gender")
    bike =  request.args.get("vehicle1")
    car =  request.args.get("vehicle2")

     
    return render_template("madlib.html",
                           person=person,
                           color=color,
                           adjective=adjective,
                           noun= noun,
                           gender = gender,
                           bike = bike,
                           car = car)



if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
