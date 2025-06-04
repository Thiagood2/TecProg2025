/* Sumar Elemento a Elemento de 2 Listas*/
% Reglas
suma_lista([], [], []).
suma_lista([X| L1], [Y | L2], [ Sum |ListaSum]):- Sum is X + Y, suma_lista(L1, L2,ListaSum).

