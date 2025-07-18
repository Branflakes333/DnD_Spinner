import pandas as pd
import numpy as np

class spinner:
    probabilities = pd.DataFrame({'outcome': [], 'probability': []})

    def __init__(self, probabilities):
        try:
            self.check_probabilities(probabilities)
        except ValueError as e:
            print(f"Invalid probabilities: {e}")
            return
        else: self.probabilities = probabilities


    def check_probabilities(self, probabilities: pd.DataFrame):
        if not isinstance(probabilities, pd.DataFrame):
            raise ValueError("Probabilities must be a pandas DataFrame")

        if probabilities.empty:
            raise ValueError("Probabilities DataFrame is empty")

        if not all(probabilities['prob'].between(0, 1)):
            raise ValueError("All probabilities must be between 0 and 1")

        if not np.isclose(probabilities['prob'].sum(), 1):
            raise ValueError("Probabilities must sum to 1")

    def spin(self):
        pass

def create_probabilities():
    outcomes = []
    exit = True
    while exit:
        outcome =  input("Enter outcome (or 'exit' to finish): ")
        if outcome.lower() == 'exit':
            exit = False
        else:
            outcomes.append(outcome)
    outcomes = list(set(outcomes))  # Remove duplicates

    probabilities = []
    odex = 0
    while odex < len(outcomes):
        if odex == len(outcomes)-1:  # If it's the last index, set probability to 1-(probs)
            prob = 1 - sum(probabilities)
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
        probabilities.append(prob)

    # Create a DataFrame from the outcomes and probabilities
    probs_df = pd.DataFrame({'outcome': outcomes, 'probability': probabilities})
    return probs_df