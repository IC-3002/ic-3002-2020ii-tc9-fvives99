def exchange(i,j,arr):
    temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
    
def quicksort(low,high,arr):
    i , j = low , high
    pivot = arr[(low + (high-low)//2)]
    while (i <= j): # If the current value from the left list is smaller than the pivot
        while (arr[i][1] < pivot[1]):# element then get the next element from the left list
            i+=1 #If the current value from the right list is larger than the pivot
        while (arr[j][1] > pivot[1]):
            j-=1;
        if (i <= j):
            exchange(i, j, arr)
            i+=1
            j-=1
    if (low < j): #recursion
        quicksort(low, j,arr)
    if (i < high):
        quicksort(i, high,arr)

def maximizar(As, D):
    almacenamiento = 0
    archivos =[]
    n=len(As)
    quicksort(0,n-1,As)
    for iterador in range(0,n):
        if almacenamiento + As[iterador][1]<=D:
            archivos.append(As[iterador])
            almacenamiento += As[iterador][1]
        else:
            return archivos
