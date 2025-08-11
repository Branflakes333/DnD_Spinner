from probability import *
from spinner import *
from node import *
from json_utils import *
from data_parser import *

nodes = base_nodes()

tree = SpinnerTree(nodes[0])

for outcome in tree.root.result_mapping['outcome']:
    tree.add_node(
        tree.root, nodes[1], outcome)

for outcome in tree.root.result_mapping['destination'][0].result_mapping['outcome']:
    tree.add_node(
        tree.root.result_mapping['destination'][0], nodes[2], outcome)

for outcome in tree.root.result_mapping['destination'][0].result_mapping['destination'][0].result_mapping['outcome']:
    tree.add_node(
        tree.root.result_mapping['destination'][0].result_mapping['destination'][0], nodes[3], outcome)

print(tree.spin_tree())
