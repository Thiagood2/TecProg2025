#lang racket
#!  Reescriba las siguientes expresiones, usando Let para remover las subexpresiones comunes y para mejorar la estructura del código. No realice ninguna simplificación algebraica: #!


#! En Racket, let se usa para definir variables locales dentro de un bloque de código. Dentro del cuerpo 'let', se pueden usar variables definidas en el bloque, y cuando termina el bloque, las variables ya no están disponibles.#!


#! (let ([var1 valor1] [var2 valor2] ...) cuerpo) #!


(define a 4)
(define b 60)
(define c 5)
(define Operacion 
(let ([x (/ (* 7 a) b)]
      [y (/ (* 3 a) b)])
        (+ x y x)))
Operacion


(define Operacion2
(let ([x (car (list a b c))]
      [y (cdr (list a b c))])
        (cons x y)))

Operacion2
