#Algoritmo Merge Sort - Cap. 2 - Cormen
#Exemplo de Divisão e Conquista
import math     

def mergeSort(lista, p, r):
    
    if p < r:
        
        q = (p + r) // 2

        
        mergeSort(lista, p, q)

       
        mergeSort(lista, q + 1, r)

        
        merge(lista, p, q, r)



def merge(lista, p, q, r):
    
    n1 = q - p + 1

  
    n2 = r - q

    
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)

    
    for i in range(0, n1):
        L[i] = lista[p + i]

    
    for j in range(0, n2):
        R[j] = lista[q + 1 + j]

    
    L[n1] = math.inf
    R[n2] = math.inf

    
    
    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            lista[k] = L[i]
            i += 1
        else:
            lista[k] = R[j]
            j += 1



A = [2, 3, 5, 1, 5, 9, 7, 66, 8]

mergeSort(A, 0, len(A) - 1)

print(A)    