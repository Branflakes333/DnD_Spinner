# For eventually running the script.
# currently for testing
from probability import *
from spinner import *
from node import *
from spinner_tree import *

multiclass_decision_node = {
        'outcome' : ['Monoclass','Multiclass'],
        'probability' : [0.01,0.99]
}

class_multiclass_node = {
        'outcome' : [
            'Artificer', 'Barbarian', 'Bard', 'Cleric', 
            'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue',
            'Sorcerer', 'Warlock', 'Wizard'],
        'probability' : [
            0.05,0.05,0.05,0.05,0.05,0.05,0.1,0.1,0.1,0.1,0.1,0.2
            ]
}



# test_mapping = {
#     'outcome' : ['Monoclass','Multiclass'], 
#     'destination' : [None,test_node_2]
# }

