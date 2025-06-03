% Algunos metodos que nos ayudaran para trabajar con listas

primero([Car|_], Car). % Primer elemento de la lista
segundo([_, X|_], X). % Segundo elemento de la lista

ultimo([Car], Car). % Ultimo elemento de la lista, requiere de recursion
ultimo([_| Cdr], Ultimo):- ultimo(Cdr, Ultimo).

/* Verificar si un elemento esta contenido en la lista */
miembro(X, [X|_]).
miembro(X, [_|Cdr]) :- miembro(X, Cdr).

/* Concatenar 2 listas */
concatenar([], L, L).
concatenar([X| L1], L2, [X| Resultado]) :- concatenar(L1, L2, Resultado).


/* Encontrar la cantidad de numeros positivos y negativos de una lista */

positivo(X):- X >= 0.
negativo(X):- X < 0.

evaluar([],0, 0).

evaluar([X| Lista], Pos, Neg):- positivo(X), evaluar(Lista, Pos1, Neg), Pos is Pos1 + 1. % Encuentra los positivos

evaluar([X| Lista], Pos, Neg):- negativo(X), evaluar(Lista, Pos, Neg1), Neg is Neg1 + 1. % Encuentra los negativos


