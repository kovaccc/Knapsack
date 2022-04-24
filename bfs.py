import copy
from bag import Bag
from collections import deque


def breadth_first_search(max_weight, searched_items):
    queue = deque([Bag()])
    best_bag = Bag()

    while len(queue) != 0:
        current_bag = queue.popleft()

        if len(current_bag.items) >= len(searched_items):
            continue

        bag_inc = current_bag.addItem(searched_items[len(current_bag.items)])
        not_inc_item = copy.copy(searched_items[len(current_bag.items)])
        not_inc_item.included = False
        bag_not_inc = current_bag.addItem(not_inc_item)

        if bag_inc.totalWeight() <= max_weight:
            queue.append(bag_inc)
            if bag_inc.totalBenefit() > best_bag.totalBenefit():
                best_bag = bag_inc

        queue.append(bag_not_inc)

    print("---BFS---" + "\n" + "Total weight:" +
          str(best_bag.totalWeight()) + "\n" + "Total benefit:"
          + str(best_bag.totalBenefit()))

    print("Items:")

    for item in best_bag.getIncludedItems():
        print(str(item.id))
