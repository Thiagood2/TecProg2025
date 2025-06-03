/* Contar Elementos de una Lista */

% Reglas
cantidad([], 0).
cantidad([X| Lista], Elementos):- cantidad(Lista, Elementos1), Elementos is Elementos1 + 1.

