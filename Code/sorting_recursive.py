#!python


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
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order
    if len(items) <= 1:
        return items
    
    half_i = len(items) // 2

    l_half, r_half = items[half_i:], items[:half_i]

    items[:] = merge(merge_sort(l_half), merge_sort(r_half))
    return items


        

def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort

if __name__ == "__main__":
    items = 'Doc Grumpy Happy Sleepy Bashful Sneezy Dopey'.split()
    print(merge_sort(items))
    print(items)
    # print(split_sort_merge(['A', 'B']))

