import random

def main(list_random):

    for i in range(0,20):
        if i == list_random.count(1):
            dictionary_main["1"]= i


    for i in range(0,20):
        if i == list_random.count(2):
            dictionary_main["2"]= i


    for i in range(0,20):
        if i == list_random.count(3):
            dictionary_main["3"]= i


    for i in range(0,20):
        if i == list_random.count(4):
            dictionary_main["4"]= i


    for i in range(0,20):
        if i == list_random.count(5):
            dictionary_main["5"]= i

def max_value(dictionary_main):

    max_value = {}
    for x,y in dictionary_main.items():
        if max(dictionary_main.values()) == y:
                max_value[x] = y
    return max_value

def min_value(max_value):
    min_value = min(max_value.items())
    
    return print(f'El numero que mas se repite es: {min_value}')
     

if __name__ == "__main__":
    list_random = sorted([random.randint(1,5) for i in range(20)]) #listado random de numeros 
    dictionary_main = {} #diccionario que recibe los resultado de la funcion main()

#funcion main() donde cada for retorna el numero de repeticiones de los numeros del 1 al 5 
    main(list_random) 
    max_value = max_value(dictionary_main)
    min_value = min_value(max_value)



print(dictionary_main) #diccionario donde se juntan los resultados de la funcion main 
print(list_random) #listado de numeros random