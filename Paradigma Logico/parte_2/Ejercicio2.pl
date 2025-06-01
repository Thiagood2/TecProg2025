% Hechos

hombre(thiago).
hombre(ricardo).
hombre(ernesto).
hombre(abu).

mujer(noni).   
mujer(triana).
mujer(lauren).
mujer(juliana).
mujer(claudia).
mujer(abi).

padre(ricardo, thiago).
padre(ricardo, triana).
padre(ricardo, lauren).
padre(ricardo, juliana).
padre(ernesto, ricardo).
padre(abu, claudia).

madre(claudia, thiago).
madre(claudia, triana).
madre(claudia, lauren).
madre(claudia, juliana).
madre(noni, ricardo).
madre(abi, claudia).

% Reglas
es_madre(Y, X):- madre(Y, X), mujer(Y).

es_padre(Y, X):- padre(Y, X), hombre(Y).

abuelo(X, Y):- padre(X, Z), padre(Z, Y), hombre(Y).

abuela(X, Y):- madre(X, Z), madre(Z, Y), mujer(Y).


hermano_varon(X,Y):- es_padre(Z, X), es_padre(Z, Y), es_madre(H, Y), es_madre(H, X), hombre(Y), X \= Y.

hermana_mujer(X,Y):- es_padre(Z, X), es_padre(Z, Y), es_madre(H, Y), es_madre(H, X), mujer(Y), X \= Y.


