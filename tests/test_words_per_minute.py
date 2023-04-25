from lib.words_per_minute import *

# I want to find out how much of a piece of text I can read based on my reading speed (WPM).
# For the purpose of this exercise I have ONLY 5 minutes spare to read.

hamlet = "O' what a rogue and peasant slave am I, is it not monstrous that this player here, but in a fiction in a dream of passion could force his soul so to his own conceit."

def test_WPM_is_not_integer():
    result = text_reader("thirty", hamlet)
    assert result == "The words per minute arguement is not an integer"

def test_WPM_is_integer():
    result = text_reader(1, hamlet)
    assert result == "O' what a rogue and"