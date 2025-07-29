from spinner import Spinner
from probability import *

class Node:
    """
    A class to represent a node in the spinner tree.
    Each node contains a Spinner and a mapping of outcomes to child nodes.
    """
    def __init__(self, spinner, result_mapping=None) -> None:
        """
        TODO after test pass; might change a lot otherwise
        """
        # Initially set attributes
        self.result_mapping = result_mapping  # dict: result -> Node
        self.spinner = spinner

        try:
            if not self.__check_Spinner__(spinner): raise TypeError
        except TypeError:
            self.spinner = Spinner() # Default spinner attr
        try:
            if not self.__check_result_mapping__(result_mapping): raise ValueError
        except ValueError:
            self.result_mapping = self.__default_result_mapping__()

    def update_spinner(self, new_spinner: Spinner, new_mapping=None) -> None:
        """
        Update the Spinner and respective result mapping

        Param:
        new_spinner (Spinner) : A Spinner object to update Node with
        new_mapping (dict) : A dict of the outcomes of the new spinner with a respective Node
        """
        if self.__check_Spinner__(new_spinner):
            self.spinner = new_spinner
            if self.__check_result_mapping__(new_mapping):
                self.result_mapping = new_mapping
            else:
                self.result_mapping = self.__default_result_mapping__()

    def update_result_mapping(self, new_mapping: dict) -> None:
        """
        Update the result mapping of the node. Think of as updating children

        Param:
        new_mapping (dict) : A dict of the outcomes of the spinner with a respective Node
        """
        if self.__check_result_mapping__(new_mapping):
            self.result_mapping = new_mapping

    # Private Helper functions
    def __check_result_mapping__(self, result_mapping : dict) -> bool:
        """
        Validates that result_mapping is a specific kind of dictionary 

        Param:
        result_mapping (dict) : dictionary that we are checking has 'outcomes' and 'destinations' as keys with lists of same length
        """
        if not isinstance(result_mapping, dict):                                    # Check input is a dict
            return False
        if 'outcome' not in result_mapping or 'destination' not in result_mapping:  # Check keys
            return False
        if len(result_mapping['outcome']) != len(result_mapping['destination']):    # Check value list lengths are equal
            return False
        if result_mapping['outcome'] != self.spinner.probabilities['outcome']:      # Check outcomes in mapping maps all outcomes in spinner
            return False
        return True

    def __default_result_mapping__(self) -> dict:
        """
        returns a default result_mapping for the current spinner attr

        Return (dict) : a dict with the same outcomes as in spinner, and all destinations are None
        """
        outcomes = self.spinner.probabilities['outcome'] # If Spinner is fine, but mapping is not, create default dict based on outcomes of spinner
        dests = [None] * len(outcomes)                   # destination for all outcomes is None
        return {'outcome':outcomes,'destination':dests}  # return a standard/default mapping for the Spinner
        
    def __check_Spinner__(self, spinner : Spinner) -> bool: # TODO Expand out more later
        """
        TODO
        """
        return isinstance(spinner, Spinner)
    
    def __eq__(self, other) -> bool: # Will be used in SpinnerTree tests
        if self.spinner == other.spinner and self.result_mapping == other.result_mapping:
            return True
        return False

# TODO
class SpinnerTree:
    """
    A class to represent a spinner tree, which can contain multiple Spinner objects.
    """

    def __init__(self, spinner: Spinner) -> None:
        self.root =  self.create_spinner_node(spinner) # The root node is the top of the tree.

    def __create_spinner_node__(self, spinner: Spinner) -> Node:
        """
        Private function to create a Node object with argument spinner
        """
        return Node(spinner)

    def add_spinner(self, probabilities: dict, outcome: str) -> None:
        """
        Adds a new Spinner to the tree with the given probabilities.
        """
        spinner_node = self.__create_spinner_node__(probabilities)
            

    # def spin_tree(self) -> list:
    #     """
    #     Spins Spinners down the tree and returns a list of outcomes.
    #     """
    #     outcomes = []

    #     def traverse(self, node, outcome=None):
    #         """
    #         A recursive function to traverse the tree and spin each Spinner.
    #         """
    #         if node.spinner is not None:
    #             outcome = node.spinner.spin()
    #             outcomes.append(outcome)
    #         for child in node.result_mapping():
    #             if node.result_mapping.key == outcome:
    #                 traverse(child['node'])

    #     traverse(self.root)
    #     return outcomes


    