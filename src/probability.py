
def check_probabilities(probabilities: dict) -> bool:
    """
    Validates the probabilities dictionary input for other functions

    Parameters
    Probabilities (dict) : dict of outcomes and probabilities

    Return (dict) : returns the original probabilities unless error is thrown
    """

    try:
        # Check if the input is a dictionary
        if not isinstance(probabilities, dict): # This also means it returns False when probabilities is type None
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
        print(e)
        return False
    else:
        return True

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
    outcomes = list(set(outcomes)) # Remove duplicates
    outcomes.sort() # Sort inplace

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


def equal_probabilities(n: int) -> list:
    """
    Returns a list of length n with all elements equal to 1/n
    """
    return [1/n] * n

def input_probabilities(lst: list, probs: list) -> dict:
    dct = {'outcome' : lst, 'probability' : probs}
    try:
        if check_probabilities(dct): return dct
        else: raise Exception
    except:
        print("Invalid input(s)")