; Obtenga el elemento X de las siguientes listas:
#lang racket

(define X (car (cdr (cdr (cdr (cdr '( a b c ​.​ x)))))))
X

(define Y (car (cdr (cdr (cdr '(a b c x))))))
Y

(define Z (car (cdr (cdr (car'((a ​.​ x) b))))))
Z

(define W (car '(x ​.​ a)))
W

(define V (car (cdr (cdr '(a ​.​ x)))))
V