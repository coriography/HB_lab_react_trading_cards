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

    # game_response = request.args.get("game_response")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_madlib_form():
    """Get user's response to game form"""

    game_response = request.args.get("response")

    if game_response == "no":
        return render_template("goodbye.html")

    if game_response == "yes":
        return render_template("game.html")


@app.route('/madlib')
def show_madlib():

    color = request.args.get("color")
    pet = request.args.get("pet")
    person = request.args.get("person")
    adjective = request.args.get("adjective")
    month = request.args.get("month")
    petname = request.args.get("petname")
    prog_lang = request.args.get("prog_lang")
    brand = request.args.get("brand")
    past_tense_verb = request.args.get("past_tense_verb")
    food = request.args.get("food")

    return render_template("madlib.html",
                            color=color,
                            pet=pet,
                            person=person,
                            adjective=adjective1,
                            adjective=adjective2,
                            adjective=adjective3,
                            adjective=adjective4,
                            adjective=adjective5,
                            month=month,
                            petname=petname,
                            prog_lang=prog_lang,
                            brand=brand,
                            past_tense_verb=past_tense_verb,
                            food=food)

     

if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
