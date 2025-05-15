; Describa los pasos necesarios para evaluar la siguiente expresión:
#lang racket


(define A ((car (cdr (cdr (list + - * /)))) 5 5))
;; Desglosando la expresion tenemos:

(define B (list + - * /))
;; list + - * / => (+ - * /)

(define C (cdr B)) 
;; (cdr (list + - * /)) => (- * /)

(define D (cdr C))
;; (cdr (cdr (list + - * /))) => (* /)

(define E (car D))
;; (car (cdr (cdr (list + - * /)))) => *

(define F (E 5 5))
;; (* 5 5) => 25

A