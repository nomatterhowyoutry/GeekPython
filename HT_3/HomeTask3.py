import random
import time

len = 10000
iList = [random.randint(0, 99) for i in range(0, len)]
fList = [random.uniform(0, 99) for i in range(0, len)]

def Bubble_Sort(A):
    start = time.time()
    for i in range(0, len):
        for j in range(i, len):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
    print('Bubble Sort time: {:.3f} sec'.format(time.time() - start), 'The list is sorted correctly = {}'.format(None == A.sort()))
    return A

Bubble_Sort(iList)
Bubble_Sort(fList)
iList = [random.randint(0, 99) for i in range(0, len)]
fList = [random.uniform(0, 99) for i in range(0, len)]

def Selection_Sort(A):
    start = time.time()
    for i in range(0, len):
        m = A.index(min(A[i:]),i,len)
        A[m], A[i] = A[i], A[m]
    print('Selection Sort time: {:.3f} sec'.format(time.time() - start), 'The list is sorted correctly = {}'.format(None == A.sort()))
    return A

Selection_Sort(iList)
Selection_Sort(fList)
iList = [random.randint(0, 99) for i in range(0, len)]
fList = [random.uniform(0, 99) for i in range(0, len)]

def Insertion_Sort(A):
    start = time.time()
    for i in range(1, len):
        j = i
        while (j > 0 and A[j] < A[j - 1]):
            A[j], A[j - 1] = A[j - 1], A[j]
            j = j - 1
    print('Insertion Sort time: {:.3f} sec'.format(time.time() - start), 'The list is sorted correctly = {}'.format(None == A.sort()))
    return A

Insertion_Sort(iList)
Insertion_Sort(fList)