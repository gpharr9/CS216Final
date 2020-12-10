# pip install flask
import flask
from Game import *

app = flask.Flask(__name__, static_folder="./static")
app.game = None

@app.route('/')
def root():
    return app.send_static_file('./index.html')
@app.route('/game')
def game():
    return app.send_static_file('./game.html')
@app.route('/main.js')
def script():
    return app.send_static_file('./main.js')
@app.route('/main.css')
def style():
    return app.send_static_file('./main.css')


@app.route('/init', methods=['POST'])
def bj_init_game():
    app.game = Game()
    game_data = generate_game_state(False)

    return flask.jsonify(game_data)

@app.route('/hit', methods=['GET'])
def bj_hit():
    app.game.validate_dealer()
    app.game.p_hit()

    p_count, d_count = app.game.get_count(display=False)

    game_state = generate_game_state(showAll=False)
    if d_count > 21 or p_count == 21:
        game_state = generate_game_state(showAll=True)
        game_state["dealer"]["count"] = d_count
        game_state["master"] = "You Win!"
    if p_count > 21:
        game_state = generate_game_state(showAll=True)
        game_state["dealer"]["count"] = d_count
        game_state["master"] = "You Lose!"

    if p_count == d_count and p_count > 21:
        game_state = generate_game_state(showAll=True)
        game_state["dealer"]["count"] = d_count
        game_state["master"] = "Tie!"
        
    return game_state
      

@app.route('/stand', methods=['GET'])
def bj_stand():
    app.game.validate_dealer()
    app.game.p_stand()

    p_count, d_count = app.game.get_count(display=False)

    game_state = generate_game_state(showAll=False)
    if p_count < d_count:
        game_state = generate_game_state(showAll=True)
        game_state["dealer"]["count"] = d_count
        game_state["master"] = "You Lose!"
    if p_count > d_count:
        game_state = generate_game_state(showAll=True)
        game_state["dealer"]["count"] = d_count
        game_state["master"] = "You Win!"
    if p_count == d_count:
        game_state = generate_game_state(showAll=True)
        game_state["dealer"]["count"] = d_count
        game_state["master"] = "Tie!"

    return game_state

def generate_game_state(showAll):
    initialCards = app.game.condition(showAll)
    initialCount = app.game.get_count(display=True)

    game_data = {
        "dealer": {
            "cards": initialCards[1],
            "count": initialCount[1]
        },
        "player": {
            "cards": initialCards[0],
            "count": initialCount[0]
        }
        
    }
    return game_data

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6969)
