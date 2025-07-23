from spinner import Spinner



class Spinner_Tree:
    """
    A class to represent a spinner tree, which can contain multiple Spinner objects.
    """

    class Node:
        """
        A class to represent a node in the spinner tree.
        Each node contains a Spinner and a mapping of outcomes to child nodes.
        """
        def __init__(self, spinner, result_mapping=None):
            self.spinner = spinner  # A Spinner object
            try:
                self.check_result_mapping(result_mapping)
            except:
                print("Invalid mapping of outcomes")
            else:
                self.result_mapping = result_mapping  # dict: result -> Node
                self.spinner = Spinner
        
        
        def check_result_mapping(result_mapping):
            if len(result_mapping.keys()) != len(result_mapping.values()):
                raise ValueError

    def __init__(self, root):
        self.root = root # Following standard tree structure, the root is a Node.

    def add_spinner(self, probabilities: dict, outcome: str) -> None:
        """
        Adds a new Spinner to the tree with the given probabilities.
        """
        spinner = Spinner(probabilities)
        if spinner.probabilities is not None:
            # If the spinner has valid probabilities, add it to the root node's children.
            self.root.result_mapping[outcome] = self.Node(spinner)

    def spin_tree(self) -> list:
        """
        Spins Spinners down the tree and returns a list of outcomes.
        """
        outcomes = []

        def traverse(node, outcome=None):
            """
            A recursive function to traverse the tree and spin each Spinner.
            """
            if node.spinner is not None:
                outcome = node.spinner.spin()
                outcomes.append(outcome)
            for child in node.result_mapping():
                if node.result_mapping.key == outcome:
                    traverse(child['node'])

        traverse(self.root)
        return outcomes


    