% Hechos

mujer(haydee).
ingeniero(haydee).
abogado(haydee).

mujer(tania).
medico(tania).

varon(pepito).
contador(pepito).

novela(rayuela).
novela(karamazov).
novela(leones).

largo(rayuela).
largo(karamazov).
corto(leones).

cuento(octaedro).
corto(octaedro).

poema(inventario).
largo(inventario).

% A los abogados le gustan las novelas largas
gusta(X, Y):- abogado(X), novela(Y), largo(Y).

% A los ingenieros y medicos le gustan las novelas
gusta(X, Y):- ingeniero(X), novela(X).
gusta(X, Y):- medico(X), novela(X).

% A las mujeres les gustan todos los libros largos
gusta(X, Y):- mujer(X), largo(Y).

% A los contadores varones le gustan tanto los libros de cuento como los libros de poema

gusta(X, Y):- varon(X), contador(X), poema(Y).
gusta(X, Y):- varon(X), contador(X), cuento(Y).


% Pedro es un abogado a quien le gustan los libros de cuentos
gusta(pedro, Y):- cuento(Y).

% Livio es un varon contador quien le gusta Rayuela
gusta(livio, rayuela).


% Libro valioso

valioso(X):- gusta(H, X), gusta(J, X), H \= J.
/* El libro mas valioso es: Rayuela. */