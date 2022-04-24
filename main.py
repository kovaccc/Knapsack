import timeit

import dfs
from item import Item
import bfs
# with deepcopy time is going over 0.5, much faster with shallow copy

with open('Assignment 1 knapsack.txt') as knapsackFile:
    knapsack_file_lines = knapsackFile.readlines()

    maxWeight = 0
    numberOfItems = 0
    items = []

    for s in knapsack_file_lines[3].split():
        if s.isdigit():
            numberOfItems = int(s)

    for s in knapsack_file_lines[4].split():
        if s.isdigit():
            maxWeight = int(s)

    for line in knapsack_file_lines[7:len(knapsack_file_lines) - 2]:
        itemLine = [int(i) for i in line.split(" ")]
        items.append(Item(item_id=itemLine[0], weight=itemLine[2], benefit=itemLine[1]))

    start = timeit.default_timer()
    bfs.breadth_first_search(max_weight=maxWeight, searched_items=items)
    stop = timeit.default_timer()
    print('BFS time: ', stop - start)
    start = timeit.default_timer()
    dfs.depth_first_search(max_weight=maxWeight, searched_items=items)
    stop = timeit.default_timer()
    print('DFS time: ', stop - start)

