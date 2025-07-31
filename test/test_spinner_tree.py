import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from unittest.mock import patch
from spinner_tree import *

def create_testers():
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
                0.05,0.05,0.05,0.05,0.05,0.05,0.1,0.1,0.1,0.1,0.1,0.2
                ]
    }

    test_new_node = Node(Spinner(test_probs_2))

    # Mapping for multiclassing outsomes
    test_mapping = {
        'outcome' : ['Monoclass','Multiclass'], 
        'destination' : [None,test_new_node]
    }

    test_node = Node(Spinner(test_probs_1), test_mapping)
    test_tree = SpinnerTree(test_node)

    return test_node, test_new_node, test_tree

def test_sprinner_tree_init():
    test_node, test_new_node, test_tree = create_testers()

    assert test_tree.root == test_node
    assert test_tree.traversal == test_node

def test_add_node():
    test_node, test_new_node, test_tree = create_testers()

    test_tree.add_node(test_tree.root,test_new_node, 'Multiclass')

    assert test_tree.traversal == test_new_node

def test_reset_traversal() -> None:
    test_node, test_new_node, test_tree = create_testers()

    test_tree.add_node(test_tree.root, test_new_node, 'Multiclass')
    test_tree.reset_traversal()
    
    assert test_tree.traversal == test_tree.root

def test_move_down_traversal():
    test_node, test_new_node, test_tree = create_testers()

    test_tree.add_node(test_tree.root, test_new_node, 'Multiclass')
    test_tree.reset_traversal()
    test_tree.move_down_traversal('Multiclass')
    assert test_tree.traversal == test_new_node

def test_spin_tree():
    test_node, test_new_node, test_tree = create_testers()
    test_tree.add_node(test_tree.root, test_new_node, 'Multiclass')

    with patch('random.random', return_value=0.95): 
        result = test_tree.spin_tree()
        assert result == ("Multiclass" , "Wizard")



