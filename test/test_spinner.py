import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from unittest.mock import patch
from spinner import *

test_probs = {
        'outcome' : [
            'Artificer', 'Barbarian', 'Bard', 'Cleric', 'Druid', 
            'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue',
            'Sorcerer', 'Warlock', 'Wizard'],
        'probability' : [
            0.05,0.05,0.05,0.05,0.05,0.05,0.1,0.1,0.1,0.1,0.1,0.1,0.1
            ]
}

# Node Tests
def test_spinner__init__():
    global test_probs
    test_spinner = Spinner(test_probs)
    assert test_spinner.probabilities == test_probs

def test_spin():
    global test_probs
    test_spinner = Spinner(test_probs)
    with patch('random.random', return_value=0.35): # Make random.random return a fixed number (0.35)
        result = test_spinner.spin()
        assert result == "Monk"

def test_update_probabilities():
    global test_probs
    test_spinner = Spinner()
    test_spinner.update_probabilities(test_probs)
    assert test_probs == test_spinner.probabilities
    
# Tree Tests
# WIP