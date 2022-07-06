import pytest
import app
from controllers import games

@pytest.fixture
def api(monkeypatch):
    test_games = [
        {'id': 1, 'name': 'Test game 1', 'players': 7},
        {'id': 2, 'name': 'Test game 2', 'players': 4}
    ]
    monkeypatch.setattr(games, "games", test_games)
    api = app.app.test_client()
    return api
