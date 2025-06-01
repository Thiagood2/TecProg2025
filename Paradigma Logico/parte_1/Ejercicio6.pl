% Hechos

estrella(sol).
orbita(sol,mercurio).
orbita(sol,venus).
orbita(sol,tierra).
orbita(sol,marte).
orbita(sol,jupiter).
orbita(sol,saturno).
orbita(sol,urano).
orbita(sol,neptuno).
orbita(sol,pluton).

orbita(tierra,luna).
orbita(mercurio, notiene).
orbita(venus, notiene).

orbita(marte,deimos).
orbita(marte,phobos).

orbita(jupiter, adrastea).
orbita(jupiter, aitne).

orbita(saturno, aegir).
orbita(saturno, albiorix).

orbita(urano, ariel).
orbita(urano, belinda).

orbita(neptuno, despina).
orbita(neptuno, galatea).

orbita(pluton, charon).
orbita(pluto,narix).

% Reglas
planeta(P):- orbita(sol,P).
luna(L):- orbita(X, L), planeta(X).
lunaDe(L, P):- orbita(P, L), planeta(P).

