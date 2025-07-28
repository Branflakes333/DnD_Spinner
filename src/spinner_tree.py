from spinner import Spinner

class Node:
    """
    A class to represent a node in the spinner tree.
    Each node contains a Spinner and a mapping of outcomes to child nodes.
    """
    def __init__(self, spinner, result_mapping=None) -> None:
        
        # Initially set attributes
        self.result_mapping = result_mapping  # dict: result -> Node
        self.spinner = spinner

        # Check and change attributes if needed
        try:
            if not self.__check_result_mapping__(result_mapping): raise ValueError
            if not self.__check_Spinner__(spinner): raise TypeError
        except ValueError:
            self.result_mapping = {'outcome' : [], 'destination' : []} # Default is an empty dict
        except TypeError:
            self.spinner = Spinner() # Default Node contains a default spinner
    
    def update_result_mapping(self, new_mapping: dict) -> None:
        """
        Update the result mapping of the node. Think of as updating children

        Param:
        new_mapping (dict) : A dict of the outcomes/results of the spinner with a respective Node
        """
        if self.__check_result_mapping__(new_mapping):
            self.result_mapping = new_mapping

    # Private Helper functions
    def __check_result_mapping__(self, result_mapping : dict) -> bool:
        if not isinstance(result_mapping, dict):
            return False
        if 'outcome' not in result_mapping or 'destination' not in result_mapping:
            return False
        return len(result_mapping['outcome']) == len(result_mapping['destination'])
    
    def __check_Spinner__(self, spinner : Spinner) -> bool:
        return isinstance(spinner, Spinner)


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


    