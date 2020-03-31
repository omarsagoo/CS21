#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    check the first item, with the item following it. if it is larger, it is not in sorted order
    Running time: 
        O(n) - worst
            has to iterate through the entire list of n items
        O(m) - best, where m is the the first occurance of the list not being sorted
            iterates through the list until it reaches a point where it is not sorted, in that case it ends
    Memory usage:  
        O(n)
            where n is the size of the list. does not create any copies.

    args:
        items - list, list of items to check if sorted
    rtrn:
        bool, If sorted True, False if not
    """
    for i in range(len(items)):
        if i + 1 == len(items):
            break
        if items[i] > items[i+1]:
            return False

    return True if all([items[i] <= items[i+1] for i in range(len(items) - 1)]) else False


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    check if the item at index i is greater than the item at index i + 1,
    if it is swap their places, continue looping until all of them are in order
    Running time:
        o(n^2) - average  full: o((n(n-1))/2)
            Iterates through the list, and for each iteration, iterates again to check for items to be sorted.
    Memory usage:
        o(n) - average
            Doesnt create any new lists or data structures, only searches and manipulates data already stored in memory
    """
    x = 1
    last_i = len(items) - 1
    for c in range(len(items)):
        

        for i in range(last_i - c):
            curr = i

            if items[i] > items[i+1]:
                items[i], items[i + 1] = items[i + 1], items[i]
                x = 1
            else:
                x += 1            

        if x >= (last_i - c):
            break






    return items
    


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items

if __name__ == "__main__":
    print(bubble_sort([2, 3, 1, 5, 4,6,9,8,7]))
    