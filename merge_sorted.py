"""
Given two sorted lists, write a function to merge them into one sorted list.

What's the time complexity?
"""
import numpy as np

# A = [1, 3, 5, 7]
# B = [2, 4, 6, 8]

A = sorted([np.random.randint(0, 100) for i in range(10)])
B = sorted([np.random.randint(0, 100) for i in range(10)])


def merge_sorted(list_a, list_b):
    a_i = b_i = 0
    list_c = []

    while(1):
        if a_i >= len(list_a) and b_i >= len(list_b):
            print('Done')
            break
        elif a_i >= len(list_a):
            list_c.append(list_b[b_i])
            b_i += 1
        elif b_i >= len(list_b):
            list_c.append(list_a[a_i])
            a_i += 1
        elif list_a[a_i] <= list_b[b_i]:
            list_c.append(list_a[a_i])
            a_i += 1
        elif list_b[b_i] < list_a[a_i]:
            list_c.append(list_b[b_i])
            b_i += 1

    return list_c


if __name__ == '__main__':
    print(A)
    print(B)

    C = merge_sorted(A, B)
    print(C)
    print('Praise the Sun')
