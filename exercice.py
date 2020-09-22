#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math 
from typing import List

def convert_to_absolute() -> float:
    #nombre = input("Entrez un nombre: ")
    #abs_nombre = abs(int(nombre))
    return abs(float(input("Entrez un numero:")))


def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOPQ', 'ack'
    
    nom = []
    for letter in prefixes : 
        nom.append(letter + suffixes)

    return nom


def prime_integer_summation() -> int:

    primes = []
    i = 2 

    while len(primes) < 100 : 
        is_prime = True 

        for divider in range(2, int(math.sqrt(i)) + 1) : 
            if i % divider == 0 : 
                is_prime = False 
                break
        
        if is_prime : 
            primes.append(i) 

        i += 1

    return sum(primes)


def factorial(number: int) -> int:
    number = int(input("Entrez un nombre: "))
    factorial = 1 

    for i in range(1, number + 1) : 
        factorial = factorial*i 

    #source : https://www.programiz.com/python-programming/examples/factorial

    return factorial 


def use_continue() -> None:

    for i in range(1, 11) : 
        if i == 5 : 
            continue 
        print(i)

    pass 


def main() -> None:
    print(f"La valeur absolue du nombre est: {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des nombres de 0 à 100 est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
