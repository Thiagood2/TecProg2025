
#! #!Defina una función distance2d que reciba como parámetros dos puntos en el plano y devuelva su distancia. Utilice una lista impropia para la declaración de x e y #!
#lang racket

(define p2 '(2 . 2))
(define p1 '(1 . 1))

(define (distance2d p1 p2)
    (define x1 (car p1))
    (define y1 (cdr p1))
    (define x2 (car p2))
    (define y2 (cdr p2))
    (define operacion (sqrt (+ (expt (- x2 x1) 2) (expt (- y2 y1 ) 2))))
    operacion)
(distance2d p1 p2)

