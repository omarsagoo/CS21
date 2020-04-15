#!python
from collections import deque


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    Running time: 
        best: O(1) - if the list is empty, or if it is a list of the same number
        average: O(n + k) - where k is the range of the numbers in the list.   (best if k < n)
    Memory usage: 
        average: O(k) - where k is the range of the numbers in the list."""
    # base case, if the list is empty or only has one item in it, then it is already sorted
    if len(numbers)  <= 1:
        return

    # find the max and the min value inside of the list.
    max_num, min_num = max(numbers), min(numbers)

    # base case, if the max and the min num in the list are the same, 
    # then all of the items in the list are the same.
    if max_num == min_num:
        return

    # create  a list of 0's with a length of the range of the numbers.
    freq_of_nums = [0] * (max_num - min_num + 1)
    
    # iterate through numbers and increment each coressponding value by 1.
    for num in numbers:
        freq_of_nums[num - min_num] += 1

    # enumerate through the frequency list, and mutate the original list with the appropriate values.
    j = 0
    for i, num in enumerate(freq_of_nums):
        if num != 0:
           for _ in range(num):
               numbers[j] = min_num + i
               j += 1
               
def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
     # base case, if the list is empty or only has one item in it, then it is already sorted
    if len(numbers)  <= 1:
        return

    # find the max and the min value inside of the list.
    max_num, min_num = max(numbers), min(numbers)

    # base case, if the max and the min num in the list are the same, 
    # then all of the items in the list are the same.
    if max_num == min_num:
        return

    # create  a list of 0's with a length of the range of the numbers.
    buckets = [0] * num_buckets
    for num in numbers:
        if buckets[(num * max_num) % num_buckets] == 0:
            bucket = deque()
            bucket.append(num)
            print(bucket)
            buckets[(num * max_num) % num_buckets] = bucket
        else:
            buckets[(num * max_num) % num_buckets].append(num)



    print(buckets)

if __name__ == "__main__":
    print(bucket_sort([3,5,3,2,3,6,7,9,18, 26,9]))
    # d = deque()
    # d.append(1)
    # d.append(3)
    # d.insert(1, 2)
    # print(d)