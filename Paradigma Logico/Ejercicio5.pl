% Hechos
ruta(santafe,parana).
ruta(parana, corrientes).
ruta(santafe, cordoba).
ruta(santafe, coronda).
ruta(santafe,rosario).
ruta(rosario,capital).
ruta(rosario,mardelplata).
ruta(capital, cordoba).

% Reglas
combinacionrutas(X,Y) :- ruta(X,Z), ruta(Z,Y).

/* Primer Consulta: ruta(X,cordoba) --> retorna X = santafe, X = capital. */
/* Segunda Consulta: ruta(parana, X) --> retorna X = corrientes. */
/* Tercer Consulta: ruta(parana,cordoba) --> retorna False. */
/* Cuarta Consulta: combinacionrutas(santafe,cordoba) --> Return true. */