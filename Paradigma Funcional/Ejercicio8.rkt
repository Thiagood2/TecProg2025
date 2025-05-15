
#! Defina una función que devuelva el área de un círculo. Ej: (area 3) → 28.26 #!

#lang racket

(define (area radio)
    (define operacion (* 3.14 (* radio radio)))
    operacion)

(area 3)