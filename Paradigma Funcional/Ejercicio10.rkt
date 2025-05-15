#lang racket
#!  Escriba una función largo que devuelva el largo de una lista sin utilizar la función definida en Racket!#!

(define (largo lista)
    (if (null? lista) ;Si la lista esta vacia, retorna 0. 
    0
    (+ 1 (largo (cdr lista)))) ; Si no, suma 1 y sigue con el resto de la lista
)

(largo '(a b c))