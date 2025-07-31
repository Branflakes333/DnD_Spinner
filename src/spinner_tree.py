from probability import *
from spinner import *
from node import *


class SpinnerTree:
    """
    A class to represent a spinner tree, which can contain multiple Spinner objects.
    """

    def __init__(self, root: Node) -> None:
        self.root =  root # Tree only keeps root node as attr. 
        self.traversal = self.root # Specifically for adding spinners

    def add_node(self,from_node, new_node: Node, outcome: str) -> None:
        """
        Adds a new Spinner to the tree by connecting it as the destination for a given outcome.
        Updates self.traversal to point to the new node.
        """
        for idx in range(len(from_node.result_mapping['outcome'])):
            if from_node.result_mapping['outcome'][idx] == outcome:
                from_node.result_mapping['destination'][idx] = new_node  # assign the new node directly
                break  # once we update, we can exit the loop

        self.traversal = new_node  # move the traversal pointer forward

    def move_down_traversal(self, outcome: str) -> None:
        for idx in range(len(self.traversal.result_mapping['outcome'])):
            if self.traversal.result_mapping['outcome'][idx] == outcome:
                self.traversal = self.traversal.result_mapping['destination'][idx] # assign the new node directly
                break
        # if error: raise KeyError # Is raising?
        

    def reset_traversal(self) -> None:
        self.traversal = self.root
    
    def spin_tree(self) -> list:
        """
        Spins Spinners down the tree and returns a list of outcomes.
        """

        def traverse(node: Node) -> str:
            """
            A recursive function to traverse the tree and spin each Spinner.
            """
            spin = node.spinner.spin()
            idx = node.result_mapping['outcome'].index(spin)
            if node.result_mapping['destination'][idx] is None:
                return spin
            else: return spin, traverse(node=node.result_mapping['destination'][idx])
        return traverse(node=self.root)


