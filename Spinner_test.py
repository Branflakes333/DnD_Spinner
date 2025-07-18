from Spinner import spinner
from Spinner import create_probabilities as create_probs
import pandas as pd

if __name__ == "__main__":
    # Example probabilities DataFrame
    probs = create_probs()
    s = spinner(probs)
    print(s.probabilities)