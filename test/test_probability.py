import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from probability import *

def test_create_probabilities(monkeypatch):
    answer = {
        'outcome' : [
            'Artificer', 'Barbarian', 'Bard', 'Cleric', 'Druid', 
            'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue',
            'Sorcerer', 'Warlock', 'Wizard'],
        'probability' : [
            0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,(1-0.1*12)
            ]}

    inputs = iter([
            'Artificer', 'Barbarian', 'Bard', 'Cleric', 'Druid', 
            'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue',
            'Sorcerer', 'Warlock', 'Wizard','exit',
            0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,(1-0.1*12)
        ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    assert create_probabilities() == answer

def test_check_bad_probabilities():
    inputs = {
        'outcome' : [
            'Artificer', 'Barbarian', 'Bard', 'Cleric', 'Druid', 
            'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue',
            'Sorcerer', 'Warlock', 'Wizard'],
        'probability' : [
            0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1
        ]}
    
    assert check_probabilities(inputs) is False

def test_check_good_probabilities():
    inputs = {
        'outcome' : [
            'Artificer', 'Barbarian', 'Bard', 'Cleric', 'Druid', 
            'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue',
            'Sorcerer', 'Warlock', 'Wizard'],
        'probability' : [
            0.05,0.05,0.05,0.05,0.05,0.05,0.1,0.1,0.1,0.1,0.1,0.1,0.1
        ]}
    
    assert check_probabilities(inputs) is True