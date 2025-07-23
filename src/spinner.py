import random

class Spinner:
    """
    Object which contains probabilities of outcomes, and can "spin" to return one of the outcomes based on the probabilities.
    """

    def __init__(self) -> None:
        self.probabilities = {'Outcome': [], 'Probability': []}

    @staticmethod
    def check_probabilities(f):
        def wrapper(probabilities: dict):
            """
            Validates the probabilities dictionary.
            """
            try:
                # Check if the input is a dictionary
                if not isinstance(probabilities, dict):
                    raise ValueError("Probabilities must be a dict")
                # Check if the dictionary has the required keys and if they are valid
                if 'outcome' not in probabilities or 'probability' not in probabilities:
                    raise ValueError("Probabilities dict must have 'outcome' and 'probability' keys")
                # Check if the outcomes and probabilities are lists of the same length
                if len(probabilities['outcome']) == 0 or len(probabilities['probability']) == 0:
                    raise ValueError("Probabilities dict is empty")
                # Check if the lengths of outcomes and probabilities match
                if len(probabilities['outcome']) != len(probabilities['probability']):
                    raise ValueError("Length of outcomes and probabilities must match")
                # Check if all probabilities are numbers between 0 and 1
                if not all(isinstance(p, (int, float)) and 0 <= p <= 1 for p in probabilities['probability']):
                    raise ValueError("All probabilities must be between 0 and 1")
                # Check if the probabilities sum to 1
                if not abs(sum(probabilities['probability']) - 1) < 1e-8:
                    raise ValueError("Probabilities must sum to 1")
            except ValueError as e:
                print(f"Invalid probabilities: {e}")
            else:
                return f(probabilities)
        return wrapper
    
    def spin(self) -> str:
        """
        Spins the spinner and returns an outcome based on the probabilities.
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

    @staticmethod # Class method to create a Spinner with user-defined probabilities
    @check_probabilities # Decorator to validate the probabilities before creating a Spinner
    def create_probabilities() -> dict:
        """
        Creates a probabilities dictionary interactively.
        """
        outcomes = []
        collecting = True
        while collecting:
            outcome = input("Enter outcome (or 'exit' to finish): ")
            if outcome.lower() == 'exit':
                collecting = False
            else:
                outcomes.append(outcome)
        outcomes = list(set(outcomes))  # Remove duplicates

        probabilities = []
        odex = 0
        while odex < len(outcomes):
            if odex == len(outcomes) - 1:  # Last index, set probability to 1 - sum
                prob = 1 - sum(probabilities)
                probabilities.append(prob)
                odex += 1
            else:
                try:
                    prob = float(input(f"Enter probability for {outcomes[odex]}: "))
                    if prob < 0 or prob > 1:
                        raise ValueError("Probability must be between 0 and 1")
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
                    continue
                else:
                    probabilities.append(prob)
                    odex += 1

        return {'outcome': outcomes, 'probability': probabilities}

    @check_probabilities
    def update_probabilities(self, new_probabilities: dict) -> None:
        """
        Updates the spinner's probabilities with a new set of probabilities.
        """
        self.probabilities = new_probabilities

