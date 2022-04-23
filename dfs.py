import copy
from queue import Queue
from bag import Bag


def depth_first_search(max_weight, searched_items):
    stack = [Bag()]
    best_bag = Bag()

    while len(stack) != 0:
        current_bag = stack.pop()

        if len(current_bag.items) >= len(searched_items):
            continue

        add_item_index = 0
        if len(current_bag.items) != 0:
            add_item_index = len(current_bag.items)

        bag_inc = current_bag.addItem(searched_items[add_item_index])
        not_inc_item = copy.copy(searched_items[add_item_index])
        not_inc_item.included = False
        bag_not_inc = current_bag.addItem(not_inc_item)

        if bag_inc.totalWeight() <= max_weight:
            stack.append(bag_inc)
            stack.append(bag_not_inc)
            if bag_inc.totalBenefit() > best_bag.totalBenefit():
                best_bag = bag_inc

    print("---DFS---" + "\n" + "Total weight:" +
          str(best_bag.totalWeight()) + "\n" + "Total benefit:"
          + str(best_bag.totalBenefit()))

    print("Items:")

    for item in best_bag.getIncludedItems():
        print(str(item.id))
