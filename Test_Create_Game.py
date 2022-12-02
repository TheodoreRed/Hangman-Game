import pytest
import Create_Game


def test_constructor():
    game = Create_Game.Game("monkey")
    assert game.word == "monkey"
