/* Eliminar Duplicados de una Lista */

/* Ejemplo:
eliminar_dup([1, 2, 3, 1, 4, 3, 5, 6], Sindup). 
SinDup = [1, 2, 3, 4, 5, 6]. */

% Reglas
miembro(X, [X|_]).
miembro(X, [_|Cdr]) :- miembro(X, Cdr).


eliminar_dup([], []).
eliminar_dup([X | L1], Sindup):- miembro(X, L1), eliminar_dup(L1, Sindup), !. % Condicion de corte pq sino tira muchas soluciones.
eliminar_dup([X | L1], [X| Sindup]):- eliminar_dup(L1, Sindup).

/* Elimino los duplicados, pero obtengo una salida distinta y es
    SinDup = [2, 1, 4, 3, 5, 6]. */
