


/* Contar la cantidad de apariciones de un valor en una Lista */
/* Se requieren de 2 reglas de (Regla de recursion) para que no se corte la Recursion */

% Reglas
esIgual(X, Y):- X == Y.
noesIgual(X, Y):- X \== Y.

contar(Valor, [], 0).
contar(Valor, [X| Lista], Cantidad):- esIgual(Valor, X), contar(Valor, Lista, Cantidad1), Cantidad is Cantidad1 + 1.
contar(Valor, [X| Lista], Cantidad):- noesIgual(Valor, X), contar(Valor, Lista, Cantidad).