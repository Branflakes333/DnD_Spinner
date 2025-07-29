import random
from probability import *

class Spinner:
    """
    Object which contains probabilities of outcomes that can "spin".
    """

    def __init__(self, probs: dict = None) -> None:
        """
        Initiate Spinner object with a probability dictionary with defaults
        """
        DEFAULT_PROBS = {'outcome': ['outcome'], 'probability': [1]}
        
        if check_probabilities(probs):
            self.probabilities = probs
        else:
            self.probabilities = DEFAULT_PROBS
            
    def spin(self) -> str:
        """
        Spins the spinner and returns an outcome based on the probabilities.
        Currently doesn't use probabilities.py
        """

        # "Spin" the spinner by generating a random number and determining the outcome based on cumulative probabilities
        spin_result = random.random()

        # Calculate cumulative probabilities and determine the outcome
        cumulative = 0
        for outcome, prob in zip(self.probabilities['outcome'], self.probabilities['probability']):
            cumulative += prob
            if spin_result < cumulative:
                return outcome
        raise Exception("No outcome selected; check probabilities.") # Shouldn't happen if probabilities are validated correctly

    def update_probabilities(self, new_probabilities: dict) -> None:
        """
        Updates the spinner's probabilities with a new set of probabilities.

        Param:
        new_probabilities (dict) : A dictionary of probabilities to update spinner's `probabilities` attribute
        """

        self.probabilities = new_probabilities if check_probabilities(new_probabilities) else self.probabilities

    def __eq__(self, other):
        """
        Allow for `==` conditional/boolean logic
        """
        if not isinstance(other, Spinner): 
            return False
        return self.probabilities == other.probabilities 
