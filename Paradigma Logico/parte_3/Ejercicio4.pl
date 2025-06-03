/* Sumar numeros de una Lista */
% Reglas
suma([],0).
suma([X| Lista], Sum):- suma(Lista, Sum1), Sum is Sum1 + X.

