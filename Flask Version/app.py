# pip install flask
import flask

app = flask.Flask(__name__, static_folder="./static")

@app.route('/')
def root():
    return app.send_static_file('./index.html')
@app.route('/main.js')
def script():
    return app.send_static_file('./main.js')
@app.route('/main.css')
def style():
    return app.send_static_file('./main.css')


@app.route('/init', methods=['POST'])
def bj_init_game():
    gameData = {
        player_cards: [],
        dealer_cards
    }
    return "initialize"

@app.route('/hit', methods=['GET'])
def bj_hit():
    return "we hittin"

@app.route('/stand', methods=['GET'])
def bj_stand():
    return "we standin"



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6969)
