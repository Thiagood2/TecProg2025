/* Filtrar numeros positivos de una Lista */
% Reglas
positivo(X):- X>=0.
positivos([], []).

/* Utilice un Corte (!) en la primer regla de recursion, porque sino me daba todas las combinaciones posibles */

positivos([X|Lista], [X|L3]):- positivo(X), positivos(Lista, L3), !.
positivos([X|Lista], L3):- positivos(Lista, L3).

