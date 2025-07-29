from spinner import Spinner
from probability import *

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


    