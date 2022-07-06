''' games controller '''
from werkzeug.exceptions import BadRequest

games = [
    {'id': 1, 'name': 'Zelda', 'players': 1},
    {'id': 2, 'name': 'Fifa', 'players': 22},
    {'id': 3, 'name': 'Warzone', 'players': 150},
]

def index(req):
    return [c for c in games], 200

def show(req, uid):
    return find_by_uid(uid), 200

def create(req):
    new_game = req.get_json()
    new_game['id'] = sorted([c['id'] for c in games])[-1] + 1
    games.append(new_game)
    return new_game, 201

def update(req, uid):
    game = find_by_uid(uid)
    data = req.get_json()
    print(data)
    for key, val in data.items():
        game[key] = val
    return game, 200

def destroy(req, uid):
    game = find_by_uid(uid)
    games.remove(game)
    return game, 204

def find_by_uid(uid):
    try:
        return next(game for game in games if game['id'] == uid)
    except:
        raise BadRequest(f"We don't have that game with id {uid}!")
