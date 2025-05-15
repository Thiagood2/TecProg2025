#! El procedimiento length retorna la longitud de su argumento, que debe ser una lista. Por ejemplo,(length '(a b c)) es 3. Usando length, defina el procedimiento mascorta, que retorna la lista más corta de los dos argumentos pasados o la primera lista si tienen el mismo largo.!#

#lang racket

(define lista1 '(1 2))
(define lista2 '(2 4))

(define  (mascorta lista1 lista2)
    (if (<= (length lista1) (length lista2))
        lista1 ;Si la longitud de lista1 es menor o igual a la de lista2, retorna lista1
        lista2)) ;Si no, (else), retorna lista2

(mascorta lista1 lista2)