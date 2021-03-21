#Algoritmo Insertion Sort - Cap 2. Cormen
def insertionSort(lista): 
                                         # custo c1 * n , onde n é o tamanho da lista
    for j in range(1,len(lista)):
        key = lista[j]                   #c2 * (n - 1)
        i = j - 1                        #c3 * (n - 1)
        while i >= 0 and lista[i] > key: #c4 * n * t, onde t = 1 no melhor caso e t = n no pior caso 
            lista[i + 1] = lista[i]      #c5 * n * (t-1)
            i = i - 1                    #c6 * n * (t-1)
        lista[i + 1] = key               #c7 * (n-1)
        
     
entrada = [2,4,6,1,3,10,54,-5,-99,99,1000,2,3,4,3,3,2,2,1,0]

print("Algoritmo Insertion Sort")

insertionSort(entrada)
print(entrada)

