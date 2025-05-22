#lang racket
#! Defina en Racket un procedimiento recursivo que encuentre el primer elemento de una lista que es un número. Debe retornar el número si lo encuentra, sino retornar null.

(define (primer-num lista)
    (cond
    [(null? lista) null] ; Si la lista es vacía, retornamos null
    [(number? (car lista)) (car lista)] ; Si el primer elemento es un número, lo retornamos
    [else (primer-num (cdr lista))])) ; Si no, llamamos recursivamente con el resto de la lista

(primer-num '((1 . 2) 'a (b) (5) 6 8 'a 9))