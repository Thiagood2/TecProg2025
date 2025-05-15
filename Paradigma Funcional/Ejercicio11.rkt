#lang racket
#!  Escriba una función que cuente la cantidad de apariciones de un elemento en una lista. El primer parámetro será el elemento a buscar y el segundo la lista en la que se debe buscar.#!

(define (count-elem valor lista)
(foldl (lambda (elem acc)
        (if (equal? elem valor) ; Si es igual el elemento al valor, incrementamos el acumulador
            (+ 1 acc)
        acc)) ;Si no es igual, lo dejamos como esta
    0       ; Acumulador inicial en cero
    lista))

(count-elem 3 '(1 2 3 4 5 4 3 2 1))
