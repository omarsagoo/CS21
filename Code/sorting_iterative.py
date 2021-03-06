#!python


def is_sorted(items, reverse=False):
    """Return a boolean indicating whether given items are in sorted order.
    check the first item, with the item following it. if it is larger, it is not in sorted order
    Running time: 
        O(n) - worst
            has to iterate through the entire list of n items
        O(m) - best, where m is the the first occurance of the list not being sorted
            iterates through the list until it reaches a point where it is not sorted, in that case it ends
    Memory usage:  
        O(1)
            where n is the size of the list. does not create any copies.

    args:
        items - list, list of items to check if sorted
        reverse - bool, False if checking in ascending arder,
                        if false checks decending order
    rtrn:
        bool, If sorted False, False if not
    """
    if reverse == False:
        for i in range(len(items) - 1):
            if items[i] > items[i+1]:
                return False
    else:
        for i in range(len(items)):
            if items[i] < items[i+1]:
                return False


    return True


def bubble_sort(items, reverse=False):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    check if the item at index i is greater than the item at index i + 1,
    if it is swap their places, continue looping until all of them are in order
    Running time:
        O(n^2) - average  full: O((n(n-1))/2)
            Iterates through the list, and for each iteration, iterates again to check for items to be sorted.
    Memory usage:
        O(1) - average
            Doesnt create any new lists or data structures, only searches and manipulates data already stored in memory

    args:
        items - list, list of items to check if sorted
        reverse - bool, False if checking in ascending arder,
                        if false checks decending order
    rtrn:
        items - list, sorted list
    """
    # sorts in ascending order if False,
    # descending if False
    if reverse == False:
        # instatiates a variable that stores the number of steps that were taken
        # if this variable reaches a number that represents the steps that would have been taken,
        # then it ends the loop.
        steps = 1
        last_i = len(items) - 1
        # initial for loop that loops over the list of n items.
        for c in range(len(items)):
            # second for loop, for each loop, loop again and check if it is sorted or not,
            # if it isnt, then it moves things appropriatley.
            for i in range(last_i - c):
                if items[i] > items[i+1]:
                    items[i], items[i + 1] = items[i + 1], items[i]
                    steps = 1
                else:
                    # if it is sorted already, incrememnt the number of steps, or reset to 1
                    steps += 1            
            # if the steps reach the number of checks that needed to be done, then break.
            if steps >= (last_i - c):
                break
        return items
    else:
        # instatiates a variable that stores the number of steps that were taken
        # if this variable reaches a number that represents the steps that would have been taken,
        # then it ends the loop.
        steps = 1
        last_i = len(items) - 1
        # initial for loop that loops over the list of n items.
        for c in range(len(items)):
            # second for loop, for each loop, loop again and check if it is sorted or not,
            # if it isnt, then it moves things appropriatley.
            for i in range(last_i - c):
                if items[i] < items[i+1]:
                    items[i], items[i + 1] = items[i + 1], items[i]
                    steps = 1
                else:
                    # if it is sorted already, incrememnt the number of steps, or reset to 1
                    steps += 1            
            # if the steps reach the number of checks that needed to be done, then break.
            if steps >= (last_i - c):
                break
        return items


def selection_sort(items, reverse=False):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Does the same for a max variable

    Running time:
        O(n^2) - average
            iterates through the list twice, and checks for both a max and a min
    Memory usage:
        O(n) - average
            uses the same list, creates tuples and overrides them.

    args:
        items - list, list of items to check if sorted
        reverse - bool, False if checking in ascending arder,
                        if false checks decending order
    rtrn:
        items - list, sorted list        
    """
    # instantiate last_i to hold the value for the last index
    last_i = len(items) - 1

    # sorts in ascending order if False,
    # Descending if False
    if reverse == False:
        # iterate through the list
        for i in range(len(items)):
            # instatiate variables to be reset every iteration
            # sets a current max num var to equal the first item in the list, which is ussually the min,
            # vice versa with min
            curr_max_num = items[0] 
            curr_min_num = items[last_i]
            # stores the index to where the max number will be swapped
            # vice versa with min
            max_index = last_i - i
            min_index = i
            # creates two tuples that store a max and min pair
            # also used to check if it is sorted
            min_pair, max_pair = ((), ())

            # iterate through the list again, enumerating and checking for the max or min pair
            for x, item in enumerate(items[i:max_index + 1]):
                if items[x+i] >= curr_max_num:
                    curr_max_num = items[x+i]
                    max_pair = (x+i, item)
                if items[x+i] <= curr_min_num:
                    curr_min_num = items[x+i]
                    min_pair = (x+i, item)

            # checks if no max/min pair was created, then breaks if True
            # also checks if the pair is the same
            if min_pair == () or max_pair == () or max_pair == min_pair:
                break

            # use the values from the tuple
            curr_min_i, curr_min_num = min_pair[0], min_pair[1]
            curr_max_i, curr_max_num = max_pair[0], max_pair[1]

            # checks the location to make sure that there is no overlapping,
            # an overlap could cause it to not sort properly
            if curr_min_i == max_index and curr_max_i == min_index:
                items[curr_min_i], items[min_index] = items[min_index], items[curr_min_i]
            elif curr_max_i == min_index:
                items[curr_max_i], items[max_index] = items[max_index], items[curr_max_i]
                items[curr_min_i], items[min_index] = items[min_index], items[curr_min_i]
            else:
                items[curr_min_i], items[min_index] = items[min_index], items[curr_min_i]
                items[curr_max_i], items[max_index] = items[max_index], items[curr_max_i]
    else:
        # iterate through the list
        for i in range(len(items)):
            # instatiate variables to be reset every iteration
            # sets a current max num var to equal the first item in the list, which is ussually the min,
            # vice versa with min
            curr_max_num = items[0] 
            curr_min_num = items[last_i]
            # stores the index to where the max number will be swapped
            # vice versa with min
            max_index = last_i - i
            min_index = 0 + i
            # creates two tuples that store a max and min pair
            # also used to check if it is sorted
            min_pair, max_pair = (), ()

            # iterate through the list again, enumerating and checking for the max or min pair
            for x, item in enumerate(items[i:max_index + 1]):
                if items[x+i] <= curr_max_num:
                    curr_max_num = items[x+i]
                    max_pair = (x+i, item)
                if items[x+i] >= curr_min_num:
                    curr_min_num = items[x+i]
                    min_pair = (x+i, item)

            # checks if no max/min pair was created, then breaks if True
            # also checks if the pair is the same
            if min_pair == () or max_pair == () or max_pair == min_pair:
                break

            # use the values from the tuple
            curr_min_i, curr_min_num = min_pair[0], min_pair[1]
            curr_max_i, curr_max_num = max_pair[0], max_pair[1]

            # checks the location to make sure that there is no overlapping,
            # an overlap could cause it to not sort properly
            if curr_min_i == max_index and curr_max_i == min_index:
                items[curr_min_i], items[min_index] = items[min_index], items[curr_min_i]
            elif curr_max_i == min_index:
                items[curr_max_i], items[max_index] = items[max_index], items[curr_max_i]
                items[curr_min_i], items[min_index] = items[min_index], items[curr_min_i]
            else:
                items[curr_min_i], items[min_index] = items[min_index], items[curr_min_i]
                items[curr_max_i], items[max_index] = items[max_index], items[curr_max_i]

        # return the list
    return items




def insertion_sort(items, reverse=False):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Running time:
        O(kn) - best avereage
            where k is the number of places each item has to be moved,
            on average the numbers are going to be displaced by a few spots.
        O(n^2) - worst
            where it iterates through the list once to the number, 
            then a second time to place it in the appropriate spot
    Memory usage: 
        O(1) - best
            doesnt create any new data structures, only uses an existing one

    args:
        items - list, list of items to check if sorted
        reverse - bool, False if checking in ascending arder,
                        if false checks decending order
    rtrn:
        items - list, sorted list
    """
    # sorts in ascending order if False,
    # descending if false
    
    if reverse == False:
        for i in range(len(items) - 1):
            m = i
            while items[m] > items[m+1] and m >= 0:
                items[m], items[m+1] = items[m+1], items[m]
                m -= 1
        return items
    else:
        for i in range(len(items) - 1):
            m = i
            while items[m] < items[m+1] and m >= 0:
                items[m], items[m+1] = items[m+1], items[m]
                m -= 1
    

if __name__ == "__main__":
    items = '5 4 3 2 1'.split()
    print(insertion_sort(items))

    