#lang racket
;  Determine el valor de la siguiente expresión

(define Operacion(let ([x 9]) ; x se define como 9
  (* x ; se multiplica x por la salida del segundo let
     (let ([x (/ x 3)]) ; en este let renombramos a x como 9/3
       (+ x x))))) ; la salida del segundo let da la suma de dos veces 3
; Conclusión esto terminara siendo la multiplicacion de 6*9
Operacion