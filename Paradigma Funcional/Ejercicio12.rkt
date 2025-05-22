#lang racket

#! Defina un procedimiento subst que reciba tres parámetros (dos valores y una lista) y devuelva la lista con todos los componentes que son iguales al primer parámetro reemplazados por el valor del segundo parámetro. Ej:(subst 'c 'k '( c o c o n u t)) → (k o k o n u t)#!


(define (subst valor1 valor2 lista)
    (map (lambda (elem)
            (if (equal? elem valor1)
                valor2
                elem))  ; Si no es igual, lo dejamos como esta
                 lista)) 


(subst 'c 'k '(c o c o n u t))