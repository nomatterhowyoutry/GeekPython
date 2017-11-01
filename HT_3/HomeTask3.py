import random
import time

iList = [random.randint(0, 99) for i in range(0, 100000)]
fList = [random.uniform(0, 99) for i in range(0, 100000)]

def Bubble_Sort(A):
    start = time.time()
    for i in range(0, len(A)):
        for j in range(i, len(A)):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
    print('Bubble Sort time: {:.3f} sec'.format(time.time() - start), 'The list is sorted correctly =', (A == sorted(A)))
    return A

Bubble_Sort(iList)
Bubble_Sort(fList)

def Selection_Sort(A):
    start = time.time()
    for i in range(0, len(A)):
        m = A.index(min(A[i:]),i,len(A))
        A[m], A[i] = A[i], A[m]
    print('Selection Sort time: {:.3f} sec'.format(time.time() - start), 'The list is sorted correctly =', (A == sorted(A)))
    return A

Selection_Sort(iList)
Selection_Sort(fList)

def Insertion_Sort(A):
    start = time.time()
    for i in range(1, len(A)):
        j = i
        while (j > 0 and A[j] < A[j - 1]):
            A[j], A[j - 1] = A[j - 1], A[j]
            j = j - 1
    print('Insertion Sort time: {:.3f} sec'.format(time.time() - start), 'The list is sorted correctly =', (A == sorted(A)))
    return A

Insertion_Sort(iList)
Insertion_Sort(fList)