import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from node import *
import random

# Spinner to decide multiclassing
test_probs_1 = {
        'outcome' : ['Monoclass','Multiclass'],
        'probability' : [0.9,0.1]
}

# Spinner to decide type of multiclassing
test_probs_2 = {
        'outcome' : [
            'Artificer', 'Barbarian', 'Bard', 'Cleric', 
            'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue',
            'Sorcerer', 'Warlock', 'Wizard'],
        'probability' : [
            0.05,0.05,0.05,0.05,0.05,0.05,0.1,0.1,0.1,0.1,0.1,0.1,0.1
            ]
}

# Mapping for multiclassing outsomes
test_mapping = {
    'outcome' : ['Monoclass','Multiclass'], 
    'destination' : [None,Node(test_probs_2)] # Technically don't need to give the spinner probabilities, but I'm diagramming the end result
}


def test_Node_init_():                                   
    global test_probs_1
    global test_mapping
    test_node = Node(spinner=Spinner(test_probs_1),result_mapping=test_mapping)
    test_spinner = Spinner(test_probs_1)
    assert test_node.spinner == test_spinner
    assert test_node.result_mapping == test_mapping 

def test_update_mapping():
    global test_probs_1
    global test_mapping
    # test_bad_map = {'outcome' : ['Monoclass','Multiclass'], 'destination' : [None,None]} # Left over line from making a bad map test <- TODO
    test_node = Node(Spinner(test_probs_1))
    test_node.update_result_mapping(test_mapping)
    assert test_node.result_mapping == test_mapping

def test_update_spinner_with_rmap():
    global test_probs_1
    global test_probs_2
    global test_mapping
    test_node = Node(Spinner(test_probs_2))
    test_node.update_spinner(Spinner(test_probs_1), test_mapping)
    assert test_node.spinner == Spinner(test_probs_1)
    assert test_node.result_mapping == test_mapping

def test_update_spinner_no_rmap():
    global test_probs_1
    global test_probs_2
    global test_mapping

    test_node = Node(Spinner(test_probs_2))
    test_node.update_spinner(Spinner(test_probs_1))

    assert test_node.spinner == Spinner(test_probs_1)
    assert test_node.result_mapping['outcome'] == ['Monoclass','Multiclass']
    assert test_node.result_mapping['destination'] == [None, None]