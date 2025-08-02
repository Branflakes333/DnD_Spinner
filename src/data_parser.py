from probability import *
from json_utils import *
from node import Node
from spinner import Spinner
from spinner_tree import SpinnerTree

_base_keys = None

def define_base_keys():
    global _base_keys 
    if _base_keys is None:
        _base_keys = retrieve_base_keys()
    return _base_keys

def base_nodes() -> list:
    base_keys = define_base_keys()
    nodes = []
    for key in base_keys:
        outcomes = retrieve_outcomes(key)
        nodes.append(
            Node(
                Spinner(
                    outcomes,
                    equal_probabilities(len(outcomes))
                )
            )
        )
    return nodes

def construct_standard_tree():
    nodes = base_nodes()
    tree = SpinnerTree
    for node in nodes:
        tree.add_node(node)
    return tree
