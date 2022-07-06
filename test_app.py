import json

class TestAPICase():
    def test_welcome(self, api):
        res = api.get('/')
        assert res.status == '200 OK'
        assert res.json['message'] == 'Hello from Flask!'

    def test_get_games(self, api):
        res = api.get('/api/games')
        assert res.status == '200 OK'
        assert len(res.json) == 2

    def test_get_game(self, api):
        res = api.get('/api/games/2')
        assert res.status == '200 OK'
        assert res.json['name'] == 'Test game 2'

    def test_get_games_error(self, api):
        res = api.get('/api/games/4')
        assert res.status == '400 BAD REQUEST'
        assert "game with id 4" in res.json['message']

    def test_post_games(self, api):
        mock_data = json.dumps({'name': 'Molly'})
        mock_headers = {'Content-Type': 'appligameion/json'}
        res = api.post('/api/games', data=mock_data, headers=mock_headers)
        assert res.json['id'] == 4

    def test_patch_game(self, api):
        mock_data = json.dumps({'id': 2, 'name': 'Zelda', 'players': 1})
        mock_headers = {'Content-Type': 'appligameion/json'}
        res = api.patch('/api/games/2', data=mock_data, headers=mock_headers)
        assert res.json['name'] == 'Zelda'

    def test_delete_game(self, api):
        res = api.delete('/api/games/1')
        assert res.status == '204 NO CONTENT'

    def test_not_found(self, api):
        res = api.get('/bob')
        assert res.status == '404 NOT FOUND'
        assert 'Oops!' in res.json['message']
