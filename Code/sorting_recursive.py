#!python
import random


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    Running time:
        O(n) - iterates through both lists only once.  
    Memory usage:
        O(n) - creates a new list of n size
    """
    
    sorted_list = []
    len_1, len_2 = len(items1), len(items2)
    i, j = 0, 0

    while i < len_1 and j < len_2:
        if items1[i] < items2[j]:
            sorted_list.append(items1[i])
            i += 1
        else:
            sorted_list.append(items2[j])
            j += 1

    sorted_list.extend(items1[i:]) 
    sorted_list.extend(items2[j:])

    return sorted_list


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    Running time: 
            O(n^2) - sorts a list by splitting it in half
    Memory usage:
            o(1) - creates constant amount of new lists
    """
    mid_index = len(items) // 2

    sorted_list = merge(sorted(items[:mid_index]), sorted(items[mid_index:]))

    items[:] = sorted_list

    return items


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    if len(items) <= 1:
        return items
    
    half_i = len(items) // 2

    l_half, r_half = items[half_i:], items[:half_i]

    items[:] = merge(merge_sort(l_half), merge_sort(r_half))
    return items


        

def partition(items, start, end):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot randomly from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    Running time:
        o(n) best  if it is nearly sorted
        o(nlogn) average
        o(n^2) worst, rarely would ever happen
    Memory usage: 
        O(1), reusing the same list"""

    pivot_index = random.randint(start, end)

    pivot = items[start]
    begin_i = start + 1
    end_i = end

    while begin_i <= end_i:
        
        while begin_i <= end_i and items[end_i] >= pivot:
            end_i -= 1

        while begin_i <= end_i and items[begin_i] <= pivot:
            begin_i += 1

        if begin_i <= end_i:
            items[begin_i], items[end_i] = items[end_i], items[begin_i]
        else:
            break

    items[start], items[end_i] = items[end_i], items[start]

    return end_i

def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    Best case running time: 
        O(nlogn) - splits the list into halves and recursively sorts.
    Worst case running time:
        O(n^2) - if the partition used is always the low or the high value
    Memory usage: 
        O(1) - reuses the same list"""

    # Check if high and low range bounds have default values (not given)
    if low is None and high is None:
        low = 0
        high = len(items) - 1

    if low < high:
        # Partition items in-place around a pivot and get index of pivot
        part = partition(items, low, high)
        # sort both halfs recursively, updating the low and the high
        quick_sort(items, low, part - 1)
        quick_sort(items, part + 1, high)

if __name__ == "__main__":
    items = 'Doc Grumpy Happy Sleepy Bashful Sneezy Dopey'.split()
    print(quick_sort(items))
    print(items)
    # print(split_sort_merge(['A', 'B']))

