#!python
from collections import deque


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    Running time: 
        best: O(1) - if the list is empty, or if it is a list of the same number
        average: O(n * k) - where k is the range of the numbers in the list.   (best if k < n)
    Memory usage: 
        average: O(k) - where k is the range of the numbers in the list.
    Args:
        numbers - array of integers"""
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
    Running time: 
        average: O(n^2)
    Memory usage: 
        average: O(k) - where k is the range of the numbers in the list.
    Args:
        numbers - array of integers"""

    if len(numbers)  <= 1:
        return

    # find the max and the min value inside of the list.
    max_num, min_num = max(numbers), min(numbers)

    # base case, if the max and the min num in the list are the same, 
    # then all of the items in the list are the same.
    if max_num == min_num:
        return

    # create  a list of lists with a length of the range of the numbers.
    buckets = [[] for _ in range(num_buckets)]
    
    for num in numbers:
        index = int(num / max_num * (num_buckets - 1))
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    index = 0
    for bucket in buckets:
        for value in bucket:
            numbers[index] = value
            index += 1
    

if __name__ == "__main__":
    items = [3,5,3,2,3,6,7,9,9,3]
    print(bucket_sort(items))
    print(items)
    # d = deque()
    # d.append(1)
    # d.append(3)
    # d.insert(1, 2)
    # print(d)