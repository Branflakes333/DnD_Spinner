# For eventually running the script.
# currently for testing
from probability import *
from spinner import *
from spinner_tree import *

test_probs_1 = {
        'outcome' : ['Monoclass','Multiclass'],
        'probability' : [0.9,0.1]
}

test_probs_2 = {
        'outcome' : [
            'Artificer', 'Barbarian', 'Bard', 'Cleric', 
            'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue',
            'Sorcerer', 'Warlock', 'Wizard'],
        'probability' : [
            0.05,0.05,0.05,0.05,0.05,0.05,0.1,0.1,0.1,0.1,0.1,0.1,0.1
            ]
}

test_mapping = {
    'outcome' : ['Monoclass','Multiclass'], 
    'destination' : [None,Node(test_probs_2)]
}

test_node = Node(spinner=test_probs_1,result_mapping= test_mapping)
test_spinner = Spinner(test_probs_1)

print()

#print(test_node.result_mapping)

print(test_spinner.__eq__(test_node.spinner))


#print(test_node.spinner.probabilities == test_spinner.probabilities)