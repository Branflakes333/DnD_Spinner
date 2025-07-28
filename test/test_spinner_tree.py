import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from spinner_tree import *
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
    'destination' : [None,Spinner(test_probs_2)] # Technically don't need to give the spinner probabilities, but I'm diagramming the end result
}


def test_Node__init__():                                   
    global test_probs_1
    global test_mapping
    test_node = Node(test_probs_1,test_mapping)
    test_attr_spinner = test_node.spinner.probabilities == test_probs_1 
    test_attr_rmap = test_node.result_mapping == test_mapping
    assert   test_attr_spinner * test_attr_rmap == 0

def test_update_mapping():
    global test_probs_1
    global test_mapping
    test_bad_map = {'outcome' : ['Monoclass','Multiclass'], 'destination' : [None,None]}
    test_node = Node(test_probs_1)
    test_node.update_result_mapping(test_mapping)
    assert test_node.result_mapping == test_mapping
