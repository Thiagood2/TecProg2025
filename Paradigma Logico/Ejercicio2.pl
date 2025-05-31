% Hechos
padre(leoncio, alberto).
padre(leoncio, geronimo).
padre(alberto, juan).
padre(alberto, luis).
padre(geronimo, luisa).

% Reglas
hermano(A,B) :- padre(X,A), padre(X,B), A\= B.
nieto(B,A) :- padre(B,X), padre(X,A).



/* Primer Consulta: padre(alberto,luis) --> return true. */
/* Segunda Consulta: padre(luis,alberto) --> return false. */
/* Tercer Consulta: hermano(luis, X) --> return X = juan. */
/* Cuarta Consulta: nieto(X, luisa) --> return X = leoncio. */
/* Quinta Consulta: nieto(X,Y) --> return X = leoncio, Y = juan ; Y = luis; Y = luisa. */