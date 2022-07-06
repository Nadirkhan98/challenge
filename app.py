from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from controllers import games
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api')
def home():

    return jsonify({'message': 'Hello from Flask!'}), 200

@app.route('/api/games', methods=['GET', 'POST'])
def games_handler():
    fns = {
        'GET': games.index,
        'POST': games.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

@app.route('/api/games/<int:game_id>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
def game_handler(game_id):
    fns = {
        'GET': games.show,
        'PATCH': games.update,
        'PUT': games.update,
        'DELETE': games.destroy
    }
    resp, code = fns[request.method](request, game_id)
    return jsonify(resp), code

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f"It's not you, it's us"}, 500

if __name__ == "__main__":
    app.run(debug=True)
