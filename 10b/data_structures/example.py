#!/opt/homebrew/bin/ python3
# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt


edgelist = [
    (0, 1),
    (1, 2),
    (1, 3),
    (2, 3),
    (2, 4),
    (3, 4),
    (4, 5),
    (4, 6),
    (6, 7)
]

labeldict = {
    0: "1",
    1: "2",
    2: "3",
    3: "4",
    4: "1",
    5: "2",
    6: "5",
    7: "3",
}

colors = [
    "red",
    "green",
    "lightblue",
    "yellow",
    "magenta",
    "pink",
    "cyan",
    "lightgreen"
]

G = nx.Graph(edgelist)

# nx.draw(
#     G,
#     node_color=colors,
#     edge_color='b',
#     labels=labeldict,
#     with_labels=True,
# )
# plt.show()

T = nx.minimum_spanning_tree(G)

nx.draw(
    T,
    node_color="red",
    edge_color='b',
    with_labels=True,
)
plt.show()
