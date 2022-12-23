import pytest
import Create_Game


def test_constructor():
    game = Create_Game.Game("monkey")
    assert game.word == "monkey"


def test_guess_spot():
    # Test that the guess_spot method correctly updates the list of correctly guessed letters
    game = Create_Game.Game("test")
    game.guess_spot("t")
    assert game.guessed_correct == ["t", "_", "_", "t"]


def test_winner():
    # Test that the winner method correctly returns True when all letters have been correctly guessed
    game = Create_Game.Game("test")
    game.guess_spot("t")
    game.guess_spot("e")
    game.guess_spot("s")
    assert game.winner() == True


def test_loser():
    # Test that the loser method correctly returns True when no more guesses are left
    game = Create_Game.Game("test")
    game.total_guesses = 0
    assert game.loser() == True


def test_get_right_guesses():
    # Test that the get_right_guesses method returns the correct number of correctly guessed letters
    game = Create_Game.Game("test")
    game.guess_spot("t")
    game.guess_spot("e")
    assert game.get_right_guesses() == 3
