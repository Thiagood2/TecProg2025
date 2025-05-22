#lang racket

#! Se desea crear un función que reciba como parámetros una lista de átomos compuesto únicamente de letras y devuelva una lista agrupando los que son iguales en sublistas. Ej: (agrupar '(A A B C A B A D C)) → ((AAAA) (BB) (CC) (D))#!

(define (agrupar lista)
  (define (agrupar-aux l acc)
    (if (null? l)
        (reverse acc)
        (let* ([elem (car l)]
               [grupo (filter (lambda (x) (equal? x elem)) l)]
               [resto (remove* grupo l)])
          (agrupar-aux resto (cons grupo acc)))))
  (agrupar-aux lista '()))

(agrupar '(A A B C A B A D C)) 